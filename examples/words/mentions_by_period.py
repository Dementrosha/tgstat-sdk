import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — число упоминаний и просмотров по периодам.
        response = await client.words.mentions_by_period(query="OpenAI")

        for item in response.items[:5]:
            print(item.period, item.mentions_count, item.views_count)


if __name__ == "__main__":
    asyncio.run(main())

