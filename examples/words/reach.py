import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — охват по периодам.
        response = await client.words.reach(query="OpenAI", group="day")

        for item in response.items[:5]:
            print(item.period, item.reach_count)


if __name__ == "__main__":
    asyncio.run(main())

