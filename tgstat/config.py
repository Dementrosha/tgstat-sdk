from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RetryConfig:
    max_attempts:   int = 5
    backoff_factor: float = 0.5
    max_backoff:    float = 5.0


@dataclass(slots=True)
class TGStatConfig:
    token:      str
    base_url:   str = "https://api.tgstat.ru"
    timeout:    float = 10.0
    user_agent: str = "tgstat-sdk/0.1.0"
    retry:      RetryConfig = field(default_factory=RetryConfig)
