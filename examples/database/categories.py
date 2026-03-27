import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — массив категорий.
        response = await client.database.categories()
        for item in response[:10]:
            print(item.code, item.name)


if __name__ == "__main__":
    asyncio.run(main())

