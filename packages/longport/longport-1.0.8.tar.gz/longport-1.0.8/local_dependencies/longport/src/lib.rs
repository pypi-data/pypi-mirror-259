#![doc = include_str!("../README.md")]
#![forbid(unsafe_code)]
#![deny(unreachable_pub)]
#![cfg_attr(docsrs, feature(doc_cfg))]
#![warn(missing_docs)]

#[macro_use]
mod macros;

mod config;
mod error;
mod serde_utils;
mod types;

#[cfg(feature = "blocking")]
#[cfg_attr(docsrs, doc(cfg(feature = "blocking")))]
pub mod blocking;
pub mod quote;
pub mod trade;

pub use config::{Config, Language};
pub use error::{Error, Result, SimpleError};
pub use longport_httpcli as httpclient;
pub use quote::QuoteContext;
pub use rust_decimal::Decimal;
pub use trade::TradeContext;
pub use types::Market;
