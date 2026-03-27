import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — периоды с общим количеством просмотров.
        response = await client.channels.views(channel_id="@durov", group="day")

        for item in response[:5]:
            print(item.period, item.views_count)


if __name__ == "__main__":
    asyncio.run(main())
