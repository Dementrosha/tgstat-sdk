from __future__ import annotations

from pydantic import Field

from ..base import TGStatModel
from ..common import Channel


class ChannelMentionItem(TGStatModel):
    mention_id:   int = Field(alias="mentionId")
    mention_type: str = Field(alias="mentionType")
    post_id:      int = Field(alias="postId")
    post_link:    str = Field(alias="postLink")
    post_date:    int = Field(alias="postDate")
    channel_id:   int = Field(alias="channelId")


class ChannelMentionsResult(TGStatModel):
    items:    list[ChannelMentionItem]
    channels: list[Channel] | None = None
