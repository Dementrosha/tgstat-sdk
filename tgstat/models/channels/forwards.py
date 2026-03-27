from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel
from ..common import Channel


class ChannelForwardItem(TGStatModel):
    forward_id:     int = Field(alias="forwardId")
    source_post_id: int = Field(alias="sourcePostId")
    post_id:        int = Field(alias="postId")
    post_link:      str = Field(alias="postLink")
    post_date:      int = Field(alias="postDate")
    channel_id:     int = Field(alias="channelId")


class ChannelForwardsResult(TGStatModel):
    items:    list[ChannelForwardItem]
    channels: list[Channel] | None = None
