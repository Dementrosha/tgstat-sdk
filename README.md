# Tgstat-sdk
[![Telegram channel](https://img.shields.io/endpoint?color=neon&url=https://tg.sumanjay.workers.dev/MoneyTherToEat)](https://t.me/MoneyTherToEat)
[![PyPI version](https://img.shields.io/pypi/v/tgstat-sdk.svg)](https://pypi.org/project/tgstat-sdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/tgstat-sdk.svg)](https://pypi.org/project/tgstat-sdk/)
[![PyPI downloads](https://img.shields.io/pypi/dm/tgstat-sdk.svg)](https://pypi.org/project/tgstat-sdk/)

Современный, удобный и асинхронный Python SDK для официального TGStat API.

Официальная документация TGStat API: [https://api.tgstat.ru/docs/](https://api.tgstat.ru/docs/)

## Что даёт библиотека

- удобный асинхронный клиент для работы с TGStat API
- единый вход через `TGStatClient`
- понятное разделение методов по ресурсам: `channels`, `posts`, `stories`, `words`, `callback`, `usage`, `database`
- типизированные модели ответов от TGStat API
- типизированные исключения для ошибок API и transport-ошибок
- готовые примеры для основных сценариев работы

## Установка

```bash
pip install -e .
```

## Быстрый старт

```python
import asyncio

from tgstat import TGStatClient
from tgstat.exceptions import TGStatError

TOKEN = "paste-your-token-here"


async def main() -> None:
    try:
        async with TGStatClient(token=TOKEN) as client:
            # Получаем информацию о канале
            channel = await client.channels.get(channel_id="@durov")
            print("Канал:", channel.title)

            # Получаем последние публикации канала
            posts = await client.channels.posts(channel_id="@durov", limit=3)
            print("Последние публикации:", len(posts.items))

            for post in posts.items:
                print("-", post.id, post.link)

            # Получаем статистику канала
            stat = await client.channels.stat(channel_id="@durov")
            print("Подписчики:", stat.participants_count)
            print("Средний охват:", stat.avg_post_reach)

            # Получаем справочник языков
            languages = await client.database.languages()
            print("Первый язык из справочника:", languages[0].name)

            # Получаем информацию о доступных квотах
            usage = await client.usage.stat()
            if usage:
                print("Тариф:", usage[0].title)

    except TGStatError as exc:
        print(f"Ошибка TGStat SDK: {exc.__class__.__name__}: {exc}")


asyncio.run(main())
```

## Что важно знать

- Некоторые методы зависят от вашего тарифа TGStat. Например, `posts.search`, `channels.search` и методы из `words.*` требуют активного доступа к Search API.
- Методы из `callback.*` требуют заранее настроенный и подтверждённый callback URL на стороне TGStat.
- Часть примеров получает реальные `post_id` и `story_id` через предварительные вызовы `channels.posts(...)` и `channels.stories(...)`, чтобы их можно было запускать без ручного поиска идентификаторов.

## Как обрабатывать ошибки

```python
from tgstat import TGStatClient
from tgstat.exceptions import InvalidTokenError, QuotaRequestsReachedError, TimeoutError

TOKEN = "paste-your-token-here"


async with TGStatClient(token=TOKEN) as client:
    try:
        await client.channels.get(channel_id="@durov")
    except InvalidTokenError:
        print("Неверный токен")
    except QuotaRequestsReachedError:
        print("Исчерпана квота запросов")
    except TimeoutError:
        print("Запрос превысил timeout")
```

## Retry

- Повторные попытки применяются только к transport-ошибкам.
- Повторяются timeout, сетевые ошибки, SSL transport failures и временные ответы `502/503/504`.
- API-ошибки вроде неверного токена, превышения квот или логических ошибок запроса не ретраятся.
- `backoff_factor` — это коэффициент задержки между повторными попытками. Чем он больше, тем быстрее растёт пауза между retry-запросами.

```python
from tgstat import RetryConfig, TGStatClient

client = TGStatClient(
    token="paste-your-token-here",
    retry=RetryConfig(
        max_attempts=4,
        backoff_factor=0.25,
        max_backoff=2.0,
    ),
)
```

## Примеры

Полная проверка SDK:

- [examples/full_sdk_check.py](examples/full_sdk_check.py)

Каналы:

- [examples/channels/get.py](examples/channels/get.py)
- [examples/channels/search.py](examples/channels/search.py)
- [examples/channels/stat.py](examples/channels/stat.py)
- [examples/channels/posts.py](examples/channels/posts.py)
- [examples/channels/stories.py](examples/channels/stories.py)
- [examples/channels/mentions.py](examples/channels/mentions.py)
- [examples/channels/forwards.py](examples/channels/forwards.py)
- [examples/channels/subscribers.py](examples/channels/subscribers.py)
- [examples/channels/views.py](examples/channels/views.py)
- [examples/channels/avg_posts_reach.py](examples/channels/avg_posts_reach.py)
- [examples/channels/er.py](examples/channels/er.py)
- [examples/channels/err.py](examples/channels/err.py)
- [examples/channels/err24.py](examples/channels/err24.py)
- [examples/channels/add.py](examples/channels/add.py)

Посты:

- [examples/posts/get.py](examples/posts/get.py)
- [examples/posts/search.py](examples/posts/search.py)
- [examples/posts/stat.py](examples/posts/stat.py)
- [examples/posts/stat_multi.py](examples/posts/stat_multi.py)

Истории:

- [examples/stories/get.py](examples/stories/get.py)
- [examples/stories/stat.py](examples/stories/stat.py)
- [examples/stories/stat_multi.py](examples/stories/stat_multi.py)

Слова:

- [examples/words/mentions.py](examples/words/mentions.py)
- [examples/words/reach.py](examples/words/reach.py)
- [examples/words/mentions_by_period.py](examples/words/mentions_by_period.py)
- [examples/words/mentions_by_channels.py](examples/words/mentions_by_channels.py)

База данных:

- [examples/database/categories.py](examples/database/categories.py)
- [examples/database/countries.py](examples/database/countries.py)
- [examples/database/languages.py](examples/database/languages.py)

Использование квот:

- [examples/usage/stat.py](examples/usage/stat.py)

Callback:

- [examples/callback/set_callback_url.py](examples/callback/set_callback_url.py)
- [examples/callback/get_callback_info.py](examples/callback/get_callback_info.py)
- [examples/callback/subscribe_channel.py](examples/callback/subscribe_channel.py)
- [examples/callback/subscribe_word.py](examples/callback/subscribe_word.py)
- [examples/callback/subscriptions_list.py](examples/callback/subscriptions_list.py)
- [examples/callback/unsubscribe.py](examples/callback/unsubscribe.py)

