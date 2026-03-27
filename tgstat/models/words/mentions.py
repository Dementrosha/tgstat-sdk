from __future__ import annotations

from ..base import TGStatModel


class WordTimelineItem(TGStatModel):
    period:         str
    mentions_count: int | None = None
    reach_count:    int | None = None


class WordMentionsPayload(TGStatModel):
    items: list[WordTimelineItem]
