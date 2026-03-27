from __future__ import annotations

from ..base import TGStatModel
from ..common import Channel, Post


class ChannelPostsResult(TGStatModel):
    count:       int | None = None
    total_count: int | None = None
    items:       list[Post]
    channel:     Channel | None = None
