import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — динамика среднего охвата публикаций.
        response = await client.channels.avg_posts_reach(channel_id="@durov", group="day")

        for item in response[:5]:
            print(item.period, item.avg_posts_reach)


if __name__ == "__main__":
    asyncio.run(main())
