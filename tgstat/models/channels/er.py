from __future__ import annotations

from ..base import TGStatModel


class ERPeriod(TGStatModel):
    period: str
    er:     float
