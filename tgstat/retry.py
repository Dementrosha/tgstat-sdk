from __future__ import annotations

import asyncio
from typing import Final

from .config import RetryConfig

DEFAULT_RETRYABLE_STATUS_CODES: Final[frozenset[int]] = frozenset({502, 503, 504})


def compute_backoff(attempt: int, config: RetryConfig) -> float:
    return min(config.backoff_factor * (2 ** max(attempt - 1, 0)), config.max_backoff)


async def sleep_before_retry(attempt: int, config: RetryConfig) -> None:
    await asyncio.sleep(compute_backoff(attempt, config))
