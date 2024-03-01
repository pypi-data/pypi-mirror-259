use time::{macros::time, Time};
use time_tz::Tz;

use crate::Type;

bitflags::bitflags! {
    #[derive(Debug, Copy, Clone)]
    pub(crate) struct UpdateFields: u32 {
        const PRICE = 0x1;
        const VOLUME = 0x2;
    }
}

#[derive(Debug, Clone, Copy, Eq, PartialEq)]
pub enum Market {
    HK,
    US,
    SH,
    SZ,
}

impl Market {
    #[inline]
    pub fn timezone(&self) -> &Tz {
        use time_tz::timezones::db;

        match self {
            Market::HK => db::asia::HONG_KONG,
            Market::US => db::america::NEW_YORK,
            Market::SH | Market::SZ => db::asia::SHANGHAI,
        }
    }

    #[inline]
    pub(crate) fn update_fields(&self, trade_type: &str) -> UpdateFields {
        match self {
            Market::HK => match trade_type {
                "" => UpdateFields::all(),
                "D" => UpdateFields::VOLUME,
                "M" => UpdateFields::VOLUME,
                "P" => UpdateFields::VOLUME,
                "U" => UpdateFields::all(),
                "X" => UpdateFields::VOLUME,
                "Y" => UpdateFields::VOLUME,
                _ => UpdateFields::empty(),
            },
            Market::US => match trade_type {
                "" => UpdateFields::all(),
                "A" => UpdateFields::all(),
                "B" => UpdateFields::all(),
                "C" => UpdateFields::VOLUME,
                "D" => UpdateFields::all(),
                "E" => UpdateFields::all(),
                "F" => UpdateFields::all(),
                "G" => UpdateFields::all(),
                "H" => UpdateFields::VOLUME,
                "I" => UpdateFields::VOLUME,
                "K" => UpdateFields::all(),
                "L" => UpdateFields::all(),
                "P" => UpdateFields::all(),
                "S" => UpdateFields::all(),
                "V" => UpdateFields::VOLUME,
                "W" => UpdateFields::VOLUME,
                "X" => UpdateFields::all(),
                "1" => UpdateFields::all(),
                _ => UpdateFields::empty(),
            },
            Market::SH | Market::SZ => UpdateFields::all(),
        }
    }

    #[inline]
    pub(crate) fn trade_sessions(&self, ty: Type) -> &'static [(Time, Time)] {
        match (self, ty) {
            (Market::HK, _) => &[
                (time!(9:30:00), time!(12:00:00)),
                (time!(13:00:00), time!(16:00:00)),
            ],
            (Market::US, Type::USOQ) => &[(time!(9:30:00), time!(16:15:00))],
            (Market::US, _) => &[(time!(9:30:00), time!(16:00:00))],
            (Market::SH | Market::SZ, _) => &[
                (time!(9:30:00), time!(11:30:00)),
                (time!(13:00:00), time!(15:00:00)),
            ],
        }
    }

    #[inline]
    pub(crate) fn half_trade_sessions(&self, ty: Type) -> &'static [(Time, Time)] {
        match (self, ty) {
            (Market::HK, _) => &[(time!(9:30:00), time!(12:00:00))],
            (Market::US, Type::USOQ) => &[(time!(9:30:00), time!(13:00:00))],
            (Market::US, _) => &[(time!(9:30:00), time!(13:00:00))],
            (Market::SH | Market::SZ, _) => unreachable!("does not supported"),
        }
    }

    #[inline]
    pub(crate) fn num_shares(&self, volume: i64) -> i64 {
        match self {
            Market::HK => volume,
            Market::US => volume,
            Market::SH => volume * 100,
            Market::SZ => volume * 100,
        }
    }
}
