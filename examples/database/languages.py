import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — массив языков.
        response = await client.database.languages()
        for item in response[:10]:
            print(item.code, item.name)


if __name__ == "__main__":
    asyncio.run(main())

