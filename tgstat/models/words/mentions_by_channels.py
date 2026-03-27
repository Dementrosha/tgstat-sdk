from __future__ import annotations

from ..base import TGStatModel
from ..common import Channel


class WordMentionsByChannelItem(TGStatModel):
    channel_id:        int
    mentions_count:    int
    views_count:       int | None = None
    last_mention_date: int | None = None


class WordMentionsByChannelsPayload(TGStatModel):
    items:    list[WordMentionsByChannelItem]
    channels: list[Channel]
