from __future__ import annotations

from ..base import TGStatModel


class SearchMentionsPeriod(TGStatModel):
    period:         str
    mentions_count: int | None = None
    views_count:    int | None = None


class WordMentionsByPeriodPayload(TGStatModel):
    items: list[SearchMentionsPeriod]
