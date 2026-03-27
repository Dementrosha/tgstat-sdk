from __future__ import annotations

from ..base import TGStatModel


class ERRPeriod(TGStatModel):
    period: str
    err:    float
