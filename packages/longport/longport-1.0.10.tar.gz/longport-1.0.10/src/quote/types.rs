use longport::quote::SubFlags;
use longport_python_macros::{PyEnum, PyObject};
use pyo3::prelude::*;

use crate::{
    decimal::PyDecimal,
    time::{PyDateWrapper, PyOffsetDateTimeWrapper, PyTimeWrapper},
    types::Market,
};

/// Subscription
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::Subscription")]
pub(crate) struct Subscription {
    symbol: String,
    #[py(sub_types)]
    sub_types: Vec<SubType>,
    #[py(array)]
    candlesticks: Vec<Period>,
}

#[pyclass]
#[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::TradeStatus")]
pub(crate) enum TradeStatus {
    /// Normal
    Normal,
    /// Suspension
    Halted,
    /// Delisted
    Delisted,
    /// Fuse
    Fuse,
    /// Prepare List
    PrepareList,
    /// Code Moved
    CodeMoved,
    /// To Be Opened
    ToBeOpened,
    /// Split Stock Halts
    SplitStockHalts,
    /// Expired
    Expired,
    /// Warrant To BeListed
    WarrantPrepareList,
    /// Warrant To BeListed
    #[py(remote = "SuspendTrade")]
    Suspend,
}

/// Trade session
#[pyclass]
#[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::TradeSession")]
pub(crate) enum TradeSession {
    /// Trading
    #[py(remote = "NormalTrade")]
    Normal,
    /// Pre-Trading
    #[py(remote = "PreTrade")]
    Pre,
    /// Post-Trading
    #[py(remote = "PostTrade")]
    Post,
}

/// Quote type of subscription
#[pyclass]
#[derive(Debug, Copy, Clone, Hash, Eq, PartialEq)]
pub(crate) enum SubType {
    /// Quote
    Quote,
    /// Depth
    Depth,
    /// Brokers
    Brokers,
    /// Trade
    Trade,
}

pub(crate) struct SubTypes(pub(crate) Vec<SubType>);

impl From<SubTypes> for SubFlags {
    fn from(types: SubTypes) -> Self {
        types
            .0
            .into_iter()
            .map(|ty| match ty {
                SubType::Quote => SubFlags::QUOTE,
                SubType::Depth => SubFlags::DEPTH,
                SubType::Brokers => SubFlags::BROKER,
                SubType::Trade => SubFlags::TRADE,
            })
            .fold(SubFlags::empty(), |mut acc, flag| {
                acc |= flag;
                acc
            })
    }
}

impl From<SubFlags> for SubTypes {
    fn from(flags: SubFlags) -> Self {
        let mut res = Vec::new();
        if flags.contains(SubFlags::QUOTE) {
            res.push(SubType::Quote);
        }
        if flags.contains(SubFlags::DEPTH) {
            res.push(SubType::Quote);
        }
        if flags.contains(SubFlags::BROKER) {
            res.push(SubType::Quote);
        }
        if flags.contains(SubFlags::TRADE) {
            res.push(SubType::Quote);
        }
        SubTypes(res)
    }
}

/// Trade direction
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::TradeDirection")]
pub(crate) enum TradeDirection {
    /// Neutral
    Neutral,
    /// Down
    Down,
    /// Up
    Up,
}

/// Option type
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::OptionType")]
pub(crate) enum OptionType {
    /// Unknown
    Unknown,
    /// American
    American,
    /// Europe
    Europe,
}

/// Option direction
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::OptionDirection")]
pub(crate) enum OptionDirection {
    /// Unknown
    Unknown,
    /// Put
    Put,
    /// Call
    Call,
}

/// Warrant type
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::WarrantType")]
pub(crate) enum WarrantType {
    /// Unknown
    Unknown,
    /// Call
    Call,
    /// Put
    Put,
    /// Bull
    Bull,
    /// Bear
    Bear,
    /// Inline
    Inline,
}

/// Candlestick period
#[pyclass]
#[allow(non_camel_case_types)]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::Period")]
pub(crate) enum Period {
    /// Unknown
    #[py(remote = "UnknownPeriod")]
    Unknown,
    /// One Minute
    #[py(remote = "OneMinute")]
    Min_1,
    /// Five Minutes
    #[py(remote = "FiveMinute")]
    Min_5,
    /// Fifteen Minutes
    #[py(remote = "FifteenMinute")]
    Min_15,
    /// Thirty Minutes
    #[py(remote = "ThirtyMinute")]
    Min_30,
    /// Sixty Minutes
    #[py(remote = "SixtyMinute")]
    Min_60,
    /// One Day
    Day,
    /// One Week
    Week,
    /// One Month
    Month,
    /// One Year
    Year,
}

/// Candlestick adjustment type
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::AdjustType")]
pub(crate) enum AdjustType {
    /// Actual
    NoAdjust,
    /// Adjust forward
    ForwardAdjust,
}

/// Derivative type
#[pyclass]
#[derive(Debug, Copy, Clone, Hash, Eq, PartialEq)]
pub(crate) enum DerivativeType {
    /// US stock options
    Option,
    /// HK warrants
    Warrant,
}

struct DerivativeTypes(Vec<DerivativeType>);

impl From<longport::quote::DerivativeType> for DerivativeTypes {
    fn from(ty: longport::quote::DerivativeType) -> Self {
        let mut res = Vec::new();
        if ty.contains(longport::quote::DerivativeType::OPTION) {
            res.push(DerivativeType::Option);
        }
        if ty.contains(longport::quote::DerivativeType::WARRANT) {
            res.push(DerivativeType::Warrant);
        }
        DerivativeTypes(res)
    }
}

/// Security board
#[pyclass]
#[derive(Debug, PyEnum, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::SecurityBoard")]
#[allow(clippy::upper_case_acronyms)]
pub enum SecurityBoard {
    /// Unknown
    Unknown,
    /// US Main Board
    USMain,
    /// US Pink Board
    USPink,
    /// Dow Jones Industrial Average
    USDJI,
    /// Nasdsaq Index
    USNSDQ,
    /// US Industry Board
    USSector,
    /// US Option
    USOption,
    /// US Sepecial Option
    USOptionS,
    /// Hong Kong Equity Securities
    HKEquity,
    /// HK PreIPO Security
    HKPreIPO,
    /// HK Warrant
    HKWarrant,
    /// Hang Seng Index
    HKHS,
    /// HK Industry Board
    HKSector,
    /// SH Main Board(Connect)
    SHMainConnect,
    /// SH Main Board(Non Connect)
    SHMainNonConnect,
    /// SH Science and Technology Innovation Board
    SHSTAR,
    /// CN Index
    CNIX,
    /// CN Industry Board
    CNSector,
    /// SZ Main Board(Connect)
    SZMainConnect,
    /// SZ Main Board(Non Connect)
    SZMainNonConnect,
    /// SZ Gem Board(Connect)
    SZGEMConnect,
    /// SZ Gem Board(Non Connect)
    SZGEMNonConnect,
    /// SG Main Board
    SGMain,
    /// Singapore Straits Index
    STI,
    /// SG Industry Board
    SGSector,
}

/// The basic information of securities
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::SecurityStaticInfo")]
pub(crate) struct SecurityStaticInfo {
    /// Security code
    symbol: String,
    /// Security name (zh-CN)
    name_cn: String,
    /// Security name (en)
    name_en: String,
    /// Security name (zh-HK)
    name_hk: String,
    /// Exchange which the security belongs to
    exchange: String,
    /// Trading currency
    currency: String,
    /// Lot size
    lot_size: i32,
    /// Total shares
    total_shares: i64,
    /// Circulating shares
    circulating_shares: i64,
    /// HK shares (only HK stocks)
    hk_shares: i64,
    /// Earnings per share
    eps: PyDecimal,
    /// Earnings per share (TTM)
    eps_ttm: PyDecimal,
    /// Net assets per share
    bps: PyDecimal,
    /// Dividend yield
    dividend_yield: PyDecimal,
    /// Types of supported derivatives
    #[py(derivative_types)]
    stock_derivatives: Vec<DerivativeType>,
    /// Board
    board: SecurityBoard,
}

/// Quote of US pre/post market
#[pyclass]
#[derive(Debug, PyObject, Copy, Clone)]
#[py(remote = "longport::quote::PrePostQuote")]
pub(crate) struct PrePostQuote {
    /// Latest price
    last_done: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Close of the last trade session
    prev_close: PyDecimal,
}

/// Quote of securitity
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::SecurityQuote")]
pub(crate) struct SecurityQuote {
    /// Security code
    symbol: String,
    /// Latest price
    last_done: PyDecimal,
    /// Yesterday's close
    prev_close: PyDecimal,
    /// Open
    open: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Security trading status
    trade_status: TradeStatus,
    /// Quote of US pre market
    #[py(opt)]
    pre_market_quote: Option<PrePostQuote>,
    /// Quote of US post market
    #[py(opt)]
    post_market_quote: Option<PrePostQuote>,
}

/// Quote of option
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::OptionQuote")]
pub(crate) struct OptionQuote {
    /// Security code
    symbol: String,
    /// Latest price
    last_done: PyDecimal,
    /// Yesterday's close
    prev_close: PyDecimal,
    /// Open
    open: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Security trading status
    trade_status: TradeStatus,
    /// Implied volatility
    implied_volatility: PyDecimal,
    /// Number of open positions
    open_interest: i64,
    /// Exprity date
    expiry_date: PyDateWrapper,
    /// Strike price
    strike_price: PyDecimal,
    /// Contract multiplier
    contract_multiplier: PyDecimal,
    /// Option type
    contract_type: OptionType,
    /// Contract size
    contract_size: PyDecimal,
    /// Option direction
    direction: OptionDirection,
    /// Underlying security historical volatility of the option
    historical_volatility: PyDecimal,
    /// Underlying security symbol of the option
    underlying_symbol: String,
}

/// Quote of warrant
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::WarrantQuote")]
pub(crate) struct WarrantQuote {
    /// Security code
    symbol: String,
    /// Latest price
    last_done: PyDecimal,
    /// Yesterday's close
    prev_close: PyDecimal,
    /// Open
    open: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Security trading status
    trade_status: TradeStatus,
    /// Implied volatility
    implied_volatility: PyDecimal,
    /// Exprity date
    expiry_date: PyDateWrapper,
    /// Last tradalbe date
    last_trade_date: PyDateWrapper,
    /// Outstanding ratio
    outstanding_ratio: PyDecimal,
    /// Outstanding quantity
    outstanding_quantity: i64,
    /// Conversion ratio
    conversion_ratio: PyDecimal,
    /// Warrant type
    category: WarrantType,
    /// Strike price
    strike_price: PyDecimal,
    /// Upper bound price
    upper_strike_price: PyDecimal,
    /// Lower bound price
    lower_strike_price: PyDecimal,
    /// Call price
    call_price: PyDecimal,
    /// Underlying security symbol of the warrant
    underlying_symbol: String,
}

/// Depth
#[pyclass]
#[derive(Debug, PyObject, Copy, Clone)]
#[py(remote = "longport::quote::Depth")]
pub(crate) struct Depth {
    /// Position
    position: i32,
    /// Price
    price: PyDecimal,
    /// Volume
    volume: i64,
    /// Number of orders
    order_num: i64,
}

/// Security depth
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::SecurityDepth")]
pub(crate) struct SecurityDepth {
    /// Ask depth
    #[py(array)]
    asks: Vec<Depth>,
    /// Bid depth
    #[py(array)]
    bids: Vec<Depth>,
}

/// Brokers
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::Brokers")]
pub(crate) struct Brokers {
    /// Position
    position: i32,
    /// Broker IDs
    broker_ids: Vec<i32>,
}

/// Security brokers
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::SecurityBrokers")]
pub(crate) struct SecurityBrokers {
    /// Ask brokers
    #[py(array)]
    ask_brokers: Vec<Brokers>,
    /// Bid brokers
    #[py(array)]
    bid_brokers: Vec<Brokers>,
}

/// Participant info
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::ParticipantInfo")]
pub(crate) struct ParticipantInfo {
    /// Broker IDs
    broker_ids: Vec<i32>,
    /// Participant name (zh-CN)
    name_cn: String,
    /// Participant name (en)
    name_en: String,
    /// Participant name (zh-HK)
    name_hk: String,
}

/// Trade
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::Trade")]
pub(crate) struct Trade {
    /// Price
    price: PyDecimal,
    /// Volume
    volume: i64,
    /// Time of trading
    timestamp: PyOffsetDateTimeWrapper,
    /// Trade type
    trade_type: String,
    /// Trade direction
    direction: TradeDirection,
    /// Trade session
    trade_session: TradeSession,
}

/// Intraday line
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::IntradayLine")]
pub(crate) struct IntradayLine {
    /// Close price of the minute
    price: PyDecimal,
    /// Start time of the minute
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Average price
    avg_price: PyDecimal,
}

/// Candlestick
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::Candlestick")]
pub(crate) struct Candlestick {
    /// Close price
    close: PyDecimal,
    /// Open price
    open: PyDecimal,
    /// Low price
    low: PyDecimal,
    /// High price
    high: PyDecimal,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Timestamp
    timestamp: PyOffsetDateTimeWrapper,
}

/// Strike price info
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::StrikePriceInfo")]
pub(crate) struct StrikePriceInfo {
    /// Strike price
    price: PyDecimal,
    /// Security code of call option
    call_symbol: String,
    /// Security code of put option
    put_symbol: String,
    /// Is standard
    standard: bool,
}

/// Issuer info
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::IssuerInfo")]
pub(crate) struct IssuerInfo {
    /// Issuer ID
    issuer_id: i32,
    /// Issuer name (zh-CN)
    name_cn: String,
    /// Issuer name (en)
    name_en: String,
    /// Issuer name (zh-HK)
    name_hk: String,
}

/// The information of trading session
#[pyclass]
#[derive(Debug, PyObject, Copy, Clone)]
#[py(remote = "longport::quote::TradingSessionInfo")]
pub(crate) struct TradingSessionInfo {
    /// Being trading time
    begin_time: PyTimeWrapper,
    /// End trading time
    end_time: PyTimeWrapper,
    /// Trading session
    trade_session: TradeSession,
}

/// Market trading session
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::MarketTradingSession")]
pub(crate) struct MarketTradingSession {
    /// Market
    market: Market,
    /// Trading sessions
    #[py(array)]
    trade_sessions: Vec<TradingSessionInfo>,
}

/// Real-time quote
#[pyclass]
#[derive(PyObject, Debug, Clone)]
#[py(remote = "longport::quote::RealtimeQuote")]
pub struct RealtimeQuote {
    /// Security code
    symbol: String,
    /// Latest price
    last_done: PyDecimal,
    /// Open
    open: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Security trading status
    trade_status: TradeStatus,
}

/// Push real-time quote
#[pyclass]
#[derive(PyObject)]
#[py(remote = "longport::quote::PushQuote")]
#[derive(Debug, Clone)]
pub struct PushQuote {
    /// Latest price
    last_done: PyDecimal,
    /// Open
    open: PyDecimal,
    /// High
    high: PyDecimal,
    /// Low
    low: PyDecimal,
    /// Time of latest price
    timestamp: PyOffsetDateTimeWrapper,
    /// Volume
    volume: i64,
    /// Turnover
    turnover: PyDecimal,
    /// Security trading status
    trade_status: TradeStatus,
    /// Trade session,
    trade_session: TradeSession,
}

/// Push real-time depth
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::PushDepth")]
pub(crate) struct PushDepth {
    /// Ask depth
    #[py(array)]
    asks: Vec<Depth>,
    /// Bid depth
    #[py(array)]
    bids: Vec<Depth>,
}

/// Push real-time brokers
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::PushBrokers")]
pub(crate) struct PushBrokers {
    /// Ask brokers
    #[py(array)]
    ask_brokers: Vec<Brokers>,
    /// Bid brokers
    #[py(array)]
    bid_brokers: Vec<Brokers>,
}

/// Push real-time trades
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::PushTrades")]
pub(crate) struct PushTrades {
    /// Trades data
    #[py(array)]
    trades: Vec<Trade>,
}

/// Push candlestick updated event
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::PushCandlestick")]
pub struct PushCandlestick {
    /// Period type
    period: Period,
    /// Candlestick
    candlestick: Candlestick,
}

/// Market trading days
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::MarketTradingDays")]
pub(crate) struct MarketTradingDays {
    /// Trading days
    #[py(array)]
    trading_days: Vec<PyDateWrapper>,
    /// Half trading days
    #[py(array)]
    half_trading_days: Vec<PyDateWrapper>,
}

/// Capital flow line
#[pyclass]
#[derive(Debug, PyObject)]
#[py(remote = "longport::quote::CapitalFlowLine")]
pub(crate) struct CapitalFlowLine {
    /// Inflow capital data
    inflow: PyDecimal,
    /// Time
    timestamp: PyOffsetDateTimeWrapper,
}

/// Capital distribution
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::CapitalDistribution")]
pub(crate) struct CapitalDistribution {
    /// Large order
    large: PyDecimal,
    /// Medium order
    medium: PyDecimal,
    /// Small order
    small: PyDecimal,
}

/// Capital distribution response
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::CapitalDistributionResponse")]
pub(crate) struct CapitalDistributionResponse {
    /// Time
    timestamp: PyOffsetDateTimeWrapper,
    /// Inflow capital data
    capital_in: CapitalDistribution,
    /// Outflow capital data
    capital_out: CapitalDistribution,
}

/// Watch list group
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::WatchlistGroup")]
pub(crate) struct WatchlistGroup {
    /// Group id
    pub id: i64,
    /// Group name
    pub name: String,
    /// Securities
    #[py(array)]
    securities: Vec<WatchlistSecurity>,
}

/// Watch list security
#[pyclass]
#[derive(Debug, PyObject, Clone)]
#[py(remote = "longport::quote::WatchlistSecurity")]
pub(crate) struct WatchlistSecurity {
    /// Security symbol
    symbol: String,
    /// Market
    market: Market,
    /// Security name
    name: String,
    /// Watched price
    #[py(opt)]
    watched_price: Option<PyDecimal>,
    /// Watched time
    watched_at: PyOffsetDateTimeWrapper,
}

/// Securities update mode
#[pyclass]
#[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::SecuritiesUpdateMode")]
pub(crate) enum SecuritiesUpdateMode {
    /// Add securities
    Add,
    /// Remove securities
    Remove,
    /// Replace securities
    Replace,
}

/// Calc index
#[pyclass]
#[derive(PyEnum, Debug, Copy, Clone, Hash, Eq, PartialEq)]
#[py(remote = "longport::quote::CalcIndex")]
pub(crate) enum CalcIndex {
    /// Latest price
    LastDone,
    /// Change value
    ChangeValue,
    /// Change rate
    ChangeRate,
    /// Volume
    Volume,
    /// Turnover
    Turnover,
    /// Year-to-date change ratio
    YtdChangeRate,
    /// Turnover rate
    TurnoverRate,
    /// Total market value
    TotalMarketValue,
    /// Capital flow
    CapitalFlow,
    /// Amplitude
    Amplitude,
    /// Volume ratio
    VolumeRatio,
    /// PE (TTM)
    PeTtmRatio,
    /// PB
    PbRatio,
    /// Dividend ratio (TTM)
    DividendRatioTtm,
    /// Five days change ratio
    FiveDayChangeRate,
    /// Ten days change ratio
    TenDayChangeRate,
    /// Half year change ratio
    HalfYearChangeRate,
    /// Five minutes change ratio
    FiveMinutesChangeRate,
    /// Expiry date
    ExpiryDate,
    /// Strike price
    StrikePrice,
    /// Upper bound price
    UpperStrikePrice,
    /// Lower bound price
    LowerStrikePrice,
    /// Outstanding quantity
    OutstandingQty,
    /// Outstanding ratio
    OutstandingRatio,
    /// Premium
    Premium,
    /// In/out of the bound
    ItmOtm,
    /// Implied volatility
    ImpliedVolatility,
    /// Warrant delta
    WarrantDelta,
    /// Call price
    CallPrice,
    /// Price interval from the call price
    ToCallPrice,
    /// Effective leverage
    EffectiveLeverage,
    /// Leverage ratio
    LeverageRatio,
    /// Conversion ratio
    ConversionRatio,
    /// Breakeven point
    BalancePoint,
    /// Open interest
    OpenInterest,
    /// Delta
    Delta,
    /// Gamma
    Gamma,
    /// Theta
    Theta,
    /// Vega
    Vega,
    /// Rho
    Rho,
}

/// Security calc index response
#[pyclass]
#[derive(PyObject, Debug, Clone)]
#[py(remote = "longport::quote::SecurityCalcIndex")]
pub(crate) struct SecurityCalcIndex {
    /// Security code
    symbol: String,
    /// Latest price
    #[py(opt)]
    last_done: Option<PyDecimal>,
    /// Change value
    #[py(opt)]
    change_value: Option<PyDecimal>,
    /// Change ratio
    #[py(opt)]
    change_rate: Option<f64>,
    /// Volume
    #[py(opt)]
    volume: Option<i64>,
    /// Turnover
    #[py(opt)]
    turnover: Option<PyDecimal>,
    /// Year-to-date change ratio
    #[py(opt)]
    ytd_change_rate: Option<f64>,
    /// Turnover rate
    #[py(opt)]
    turnover_rate: Option<f64>,
    /// Total market value
    #[py(opt)]
    total_market_value: Option<PyDecimal>,
    /// Capital flow
    #[py(opt)]
    capital_flow: Option<PyDecimal>,
    /// Amplitude
    #[py(opt)]
    amplitude: Option<f64>,
    /// Volume ratio
    #[py(opt)]
    volume_ratio: Option<f64>,
    /// PE (TTM)
    #[py(opt)]
    pe_ttm_ratio: Option<f64>,
    /// PB
    #[py(opt)]
    pb_ratio: Option<f64>,
    /// Dividend ratio (TTM)
    #[py(opt)]
    dividend_ratio_ttm: Option<f64>,
    /// Five days change ratio
    #[py(opt)]
    five_day_change_rate: Option<f64>,
    /// Ten days change ratio
    #[py(opt)]
    ten_day_change_rate: Option<f64>,
    /// Half year change ratio
    #[py(opt)]
    half_year_change_rate: Option<f64>,
    /// Five minutes change ratio
    #[py(opt)]
    five_minutes_change_rate: Option<f64>,
    /// Expiry date
    #[py(opt)]
    expiry_date: Option<PyDateWrapper>,
    /// Strike price
    #[py(opt)]
    strike_price: Option<PyDecimal>,
    /// Upper bound price
    #[py(opt)]
    upper_strike_price: Option<PyDecimal>,
    /// Lower bound price
    #[py(opt)]
    lower_strike_price: Option<PyDecimal>,
    /// Outstanding quantity
    #[py(opt)]
    outstanding_qty: Option<i64>,
    /// Outstanding ratio
    #[py(opt)]
    outstanding_ratio: Option<f64>,
    /// Premium
    #[py(opt)]
    premium: Option<f64>,
    /// In/out of the bound
    #[py(opt)]
    itm_otm: Option<f64>,
    /// Implied volatility
    #[py(opt)]
    implied_volatility: Option<f64>,
    /// Warrant delta
    #[py(opt)]
    warrant_delta: Option<f64>,
    /// Call price
    #[py(opt)]
    call_price: Option<PyDecimal>,
    /// Price interval from the call price
    #[py(opt)]
    to_call_price: Option<PyDecimal>,
    /// Effective leverage
    #[py(opt)]
    effective_leverage: Option<f64>,
    /// Leverage ratio
    #[py(opt)]
    leverage_ratio: Option<f64>,
    /// Conversion ratio
    #[py(opt)]
    conversion_ratio: Option<f64>,
    /// Breakeven point
    #[py(opt)]
    balance_point: Option<f64>,
    /// Open interest
    #[py(opt)]
    open_interest: Option<i64>,
    /// Delta
    #[py(opt)]
    delta: Option<f64>,
    /// Gamma
    #[py(opt)]
    gamma: Option<f64>,
    /// Theta
    #[py(opt)]
    theta: Option<f64>,
    /// Vega
    #[py(opt)]
    vega: Option<f64>,
    /// Rho
    #[py(opt)]
    rho: Option<f64>,
}
