from __future__ import annotations

from ..models.common import UsageStatItem
from ..transport import TGStatTransport


class UsageResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def stat(self) -> list[UsageStatItem]:
        """Получить статистику использования тарифов TGStat API."""
        return await self._transport.request(
            "GET",
            "/usage/stat",
            response_model=list[UsageStatItem],
        )
