from __future__ import annotations

from ..base import TGStatModel


class SubscribersPeriod(TGStatModel):
    period:             str
    participants_count: int
