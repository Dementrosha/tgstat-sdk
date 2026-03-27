from __future__ import annotations

from ..base import TGStatModel
from ..common import Channel, Story


class ChannelStoriesResult(TGStatModel):
    count:       int | None = None
    total_count: int | None = None
    items:       list[Story]
    channel:     Channel | None = None
