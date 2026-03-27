from __future__ import annotations

from ..models.common import DatabaseItem
from ..transport import TGStatTransport


class DatabaseResource:
    def __init__(
        self,
        transport: TGStatTransport,
    ) -> None:
        self._transport = transport

    async def categories(self, *, lang: str | None = None) -> list[DatabaseItem]:
        """Получить список категорий TGStat."""
        return await self._transport.request(
            "GET",
            "/database/categories",
            response_model=list[DatabaseItem],
            params={"lang": lang},
        )

    async def countries(self, *, lang: str | None = None) -> list[DatabaseItem]:
        """Получить список стран TGStat."""
        return await self._transport.request(
            "GET",
            "/database/countries",
            response_model=list[DatabaseItem],
            params={"lang": lang},
        )

    async def languages(self, *, lang: str | None = None) -> list[DatabaseItem]:
        """Получить список языков TGStat."""
        return await self._transport.request(
            "GET",
            "/database/languages",
            response_model=list[DatabaseItem],
            params={"lang": lang},
        )
