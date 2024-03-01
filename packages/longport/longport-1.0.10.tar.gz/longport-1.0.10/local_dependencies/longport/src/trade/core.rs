use std::{collections::HashSet, sync::Arc, time::Duration};

use longport_httpcli::HttpClient;
use longport_proto::trade::{Sub, SubResponse, Unsub, UnsubResponse};
use longport_wscli::{
    CodecType, Platform, ProtocolVersion, WsClient, WsClientError, WsEvent, WsSession,
};
use tokio::sync::{mpsc, oneshot};

use crate::{
    trade::{cmd_code, PushEvent, TopicType},
    Config, Result,
};

const RECONNECT_DELAY: Duration = Duration::from_secs(2);

pub(crate) enum Command {
    Subscribe {
        topics: Vec<TopicType>,
        reply_tx: oneshot::Sender<Result<()>>,
    },
    Unsubscribe {
        topics: Vec<TopicType>,
        reply_tx: oneshot::Sender<Result<()>>,
    },
}

pub(crate) struct Core {
    config: Arc<Config>,
    command_rx: mpsc::UnboundedReceiver<Command>,
    push_tx: mpsc::UnboundedSender<PushEvent>,
    event_tx: mpsc::UnboundedSender<WsEvent>,
    event_rx: mpsc::UnboundedReceiver<WsEvent>,
    http_cli: HttpClient,
    ws_cli: WsClient,
    session: Option<WsSession>,
    close: bool,
    subscriptions: HashSet<String>,
}

impl Core {
    pub(crate) async fn try_new(
        config: Arc<Config>,
        command_rx: mpsc::UnboundedReceiver<Command>,
        push_tx: mpsc::UnboundedSender<PushEvent>,
    ) -> Result<Self> {
        let http_cli = config.create_http_client();
        let otp = http_cli.get_otp_v2().await?;

        let (event_tx, event_rx) = mpsc::unbounded_channel();

        tracing::debug!(
            url = config.trade_ws_url.as_str(),
            "connecting to trade server",
        );
        let ws_cli = WsClient::open(
            config
                .create_trade_ws_request()
                .map_err(WsClientError::from)?,
            ProtocolVersion::Version1,
            CodecType::Protobuf,
            Platform::OpenAPI,
            event_tx.clone(),
            vec![],
        )
        .await?;

        tracing::debug!(url = config.trade_ws_url.as_str(), "trade server connected");

        let session = ws_cli.request_auth(otp).await?;

        Ok(Self {
            config,
            command_rx,
            push_tx,
            event_tx,
            event_rx,
            http_cli,
            ws_cli,
            session: Some(session),
            close: false,
            subscriptions: HashSet::new(),
        })
    }

    pub(crate) async fn run(mut self) {
        while !self.close {
            match self.main_loop().await {
                Ok(()) => return,
                Err(err) => tracing::error!(error = %err, "trade disconnected"),
            }

            loop {
                // reconnect
                tokio::time::sleep(RECONNECT_DELAY).await;

                tracing::debug!(
                    url = self.config.trade_ws_url.as_str(),
                    "connecting to trade server",
                );

                match WsClient::open(
                    self.config.create_trade_ws_request().unwrap(),
                    ProtocolVersion::Version1,
                    CodecType::Protobuf,
                    Platform::OpenAPI,
                    self.event_tx.clone(),
                    vec![],
                )
                .await
                {
                    Ok(ws_cli) => self.ws_cli = ws_cli,
                    Err(err) => {
                        tracing::error!(error = %err, "failed to connect trade server");
                        continue;
                    }
                }

                tracing::debug!(
                    url = self.config.trade_ws_url.as_str(),
                    "trade server connected"
                );

                // request new session
                match &self.session {
                    Some(session) if !session.is_expired() => {
                        match self.ws_cli.request_reconnect(&session.session_id).await {
                            Ok(new_session) => self.session = Some(new_session),
                            Err(err) => {
                                self.session = None; // invalid session
                                tracing::error!(error = %err, "failed to request session id");
                                continue;
                            }
                        }
                    }
                    _ => {
                        let otp = match self.http_cli.get_otp_v2().await {
                            Ok(otp) => otp,
                            Err(err) => {
                                tracing::error!(error = %err, "failed to request otp");
                                continue;
                            }
                        };

                        match self.ws_cli.request_auth(otp).await {
                            Ok(new_session) => self.session = Some(new_session),
                            Err(err) => {
                                tracing::error!(error = %err, "failed to request session id");
                                continue;
                            }
                        }
                    }
                }

                // handle reconnect
                match self.resubscribe().await {
                    Ok(()) => break,
                    Err(err) => {
                        tracing::error!(error = %err, "failed to subscribe topics");
                        continue;
                    }
                }
            }
        }
    }

    #[tracing::instrument(level = "debug", skip(self))]
    async fn main_loop(&mut self) -> Result<()> {
        loop {
            tokio::select! {
                item = self.event_rx.recv() => {
                    match item {
                        Some(event) => self.handle_ws_event(event).await?,
                        None => unreachable!(),
                    }
                }
                item = self.command_rx.recv() => {
                    match item {
                        Some(command) => self.handle_command(command).await?,
                        None => {
                            self.close = true;
                            return Ok(());
                        }
                    }
                }
            }
        }
    }

    async fn handle_ws_event(&mut self, event: WsEvent) -> Result<()> {
        match event {
            WsEvent::Error(err) => Err(err.into()),
            WsEvent::Push { command_code, body } => self.handle_push(command_code, body).await,
        }
    }

    async fn handle_push(&mut self, command_code: u8, body: Vec<u8>) -> Result<()> {
        match PushEvent::parse(command_code, &body) {
            Ok(Some(event)) => {
                let _ = self.push_tx.send(event);
            }
            Ok(None) => {}
            Err(err) => {
                tracing::error!(error = %err, "failed to parse push message")
            }
        }
        Ok(())
    }

    async fn handle_command(&mut self, command: Command) -> Result<()> {
        match command {
            Command::Subscribe { topics, reply_tx } => {
                let res = self.handle_subscribe(topics).await;
                let _ = reply_tx.send(res);
                Ok(())
            }
            Command::Unsubscribe { topics, reply_tx } => {
                let res = self.handle_unsubscribe(topics).await;
                let _ = reply_tx.send(res);
                Ok(())
            }
        }
    }

    async fn handle_subscribe(&mut self, topics: Vec<TopicType>) -> Result<()> {
        let req = Sub {
            topics: topics.iter().map(ToString::to_string).collect(),
        };
        let resp: SubResponse = self.ws_cli.request(cmd_code::SUBSCRIBE, None, req).await?;
        self.subscriptions = resp.current.into_iter().collect();
        Ok(())
    }

    async fn handle_unsubscribe(&mut self, topics: Vec<TopicType>) -> Result<()> {
        let req = Unsub {
            topics: topics.iter().map(ToString::to_string).collect(),
        };
        let resp: UnsubResponse = self
            .ws_cli
            .request(cmd_code::UNSUBSCRIBE, None, req)
            .await?;
        self.subscriptions = resp.current.into_iter().collect();

        Ok(())
    }

    async fn resubscribe(&mut self) -> Result<()> {
        let req = Sub {
            topics: self.subscriptions.iter().cloned().collect(),
        };
        let resp: SubResponse = self.ws_cli.request(cmd_code::SUBSCRIBE, None, req).await?;
        self.subscriptions = resp.current.into_iter().collect();
        Ok(())
    }
}
