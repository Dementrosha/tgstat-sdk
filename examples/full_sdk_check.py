import asyncio

from tgstat import TGStatClient
from tgstat.exceptions import NoActiveSubscriptionError, TGStatError

TOKEN = "paste-your-token-here"


async def check(name: str, coro) -> None:
    try:
        result = await coro
        print(f"[OK] {name}")
        print("     result type:", type(result).__name__)
    except NoActiveSubscriptionError as exc:
        print(f"[SKIP] {name}: {exc.__class__.__name__}: {exc}")
    except TGStatError as exc:
        print(f"[ERR] {name}: {exc.__class__.__name__}: {exc}")
    except Exception as exc:
        print(f"[ERR] {name}: {exc.__class__.__name__}: {exc}")


async def main() -> None:
    """
    Вставьте ваш TGStat API токен в TOKEN и запустите файл.
    Этот пример помогает быстро проверить работоспособность всего SDK.

    Некоторые методы зависят от вашего тарифа:
    - Search API нужен для channels.search, posts.search и words.*
    - Callback API здесь не проверяется, так как требует внешний callback URL
    """
    async with TGStatClient(token=TOKEN) as client:
        await check("database.languages", client.database.languages())
        await check("database.countries", client.database.countries())
        await check("database.categories", client.database.categories())
        await check("usage.stat", client.usage.stat())
        await check("channels.get", client.channels.get(channel_id="@durov"))
        await check("channels.stat", client.channels.stat(channel_id="@durov"))
        await check("channels.posts", client.channels.posts(channel_id="@durov", limit=3, extended=True))
        await check("channels.stories", client.channels.stories(channel_id="@durov", limit=3))
        await check("channels.mentions", client.channels.mentions(channel_id="@durov", limit=3, extended=True))
        await check("channels.forwards", client.channels.forwards(channel_id="@durov", limit=3, extended=True))
        await check("channels.subscribers", client.channels.subscribers(channel_id="@durov", group="day"))
        await check("channels.views", client.channels.views(channel_id="@durov", group="day"))
        await check("channels.avg_posts_reach", client.channels.avg_posts_reach(channel_id="@durov", group="day"))
        await check("channels.er", client.channels.er(channel_id="@durov", group="day"))
        await check("channels.err", client.channels.err(channel_id="@durov", group="day"))
        await check("channels.err24", client.channels.err24(channel_id="@durov", group="day"))
        await check("channels.search", client.channels.search(query="crypto", country="RU", limit=3))
        await check("posts.search", client.posts.search(query="bitcoin", limit=3, hide_forwards=True, extended=True))
        await check("words.mentions", client.words.mentions(query="OpenAI", group="day"))
        await check("words.reach", client.words.reach(query="OpenAI", group="day"))
        await check("words.mentions_by_period", client.words.mentions_by_period(query="OpenAI"))
        await check("words.mentions_by_channels", client.words.mentions_by_channels(query="OpenAI"))

        channel_posts = await client.channels.posts(channel_id="@durov", limit=3)
        post_ids = [post.id for post in channel_posts.items]
        if post_ids:
            await check("posts.stat_multi", client.posts.stat_multi(channel_id="@durov", posts_ids=post_ids))
        else:
            print("[SKIP] posts.stat_multi: no channel posts available")

        channel_stories = await client.channels.stories(channel_id="@durov", limit=3)
        story_ids = [story.id for story in channel_stories.items]
        if story_ids:
            await check("stories.stat_multi", client.stories.stat_multi(channel_id="@durov", stories_ids=story_ids))
        else:
            print("[SKIP] stories.stat_multi: no channel stories available")

        print("[SKIP] channels.add: skipped intentionally to avoid adding channels during full SDK check")
        print("[SKIP] callback.unsubscribe: skipped intentionally because it mutates callback subscriptions")


if __name__ == "__main__":
    asyncio.run(main())

