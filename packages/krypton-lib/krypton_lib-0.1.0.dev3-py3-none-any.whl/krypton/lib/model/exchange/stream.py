from enum import StrEnum, auto

from krypton.lib.model.base import BaseModel


class StreamType(StrEnum):
    TICKER = auto()


class StreamSource(StrEnum):
    BINANCE_SPOT = auto()


class Stream(BaseModel):
  stype: StreamType


class StreamSubscription(BaseModel):
   source: StreamSource
   stream: Stream
