import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — список периодов с количеством подписчиков.
        response = await client.channels.subscribers(channel_id="@durov", group="day")

        for item in response[:5]:
            print(item.period, item.participants_count)


if __name__ == "__main__":
    asyncio.run(main())
