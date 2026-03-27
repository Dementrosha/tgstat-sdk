import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — динамика ERR по периодам.
        response = await client.channels.err(channel_id="@durov", group="day")

        for item in response[:5]:
            print(item.period, item.err)


if __name__ == "__main__":
    asyncio.run(main())
