from __future__ import annotations

import httpx

from .config import RetryConfig, TGStatConfig
from .resources import (
    CallbackResource,
    ChannelsResource,
    DatabaseResource,
    PostsResource,
    StoriesResource,
    UsageResource,
    WordsResource,
)
from .transport import TGStatTransport


class TGStatClient:
    def __init__(
        self,
        *,
        token:       str | None = None,
        config:      TGStatConfig | None = None,
        base_url:    str | None = None,
        timeout:     float | None = None,
        user_agent:  str | None = None,
        retry:       RetryConfig | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        if config is None:
            if token is None:
                raise ValueError("Either 'token' or 'config' must be provided.")
            config = TGStatConfig(
                token=token,
                base_url=base_url or "https://api.tgstat.ru",
                timeout=timeout or 10.0,
                user_agent=user_agent or "tgstat-sdk/0.1.0",
                retry=retry or RetryConfig(),
            )

        self.config = config
        self.transport = TGStatTransport(config, client=http_client)
        self.channels = ChannelsResource(self.transport)
        self.posts = PostsResource(self.transport)
        self.stories = StoriesResource(self.transport)
        self.words = WordsResource(self.transport)
        self.callback = CallbackResource(self.transport)
        self.usage = UsageResource(self.transport)
        self.database = DatabaseResource(self.transport)

    async def __aenter__(self) -> TGStatClient:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self.transport.aclose()
