from __future__ import annotations

from ..base import TGStatModel


class ViewsPeriod(TGStatModel):
    period:      str
    views_count: int
