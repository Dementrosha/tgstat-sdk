from __future__ import annotations

from ..base import TGStatModel
from ..common import Channel


class ChannelSearchPayload(TGStatModel):
    count: int
    items: list[Channel]
