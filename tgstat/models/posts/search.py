from __future__ import annotations

from ..common import Channel, Post
from ..base import TGStatModel


class PostSearchPayload(TGStatModel):
    count:       int
    total_count: int
    items:       list[Post]
    channels:    list[Channel] | None = None
