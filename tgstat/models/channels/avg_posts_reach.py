from __future__ import annotations

from ..base import TGStatModel


class AvgPostsReachPeriod(TGStatModel):
    period:          str
    avg_posts_reach: int
