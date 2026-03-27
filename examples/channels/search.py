import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Для channels.search TGStat ожидает страну канала в параметре country.
        response = await client.channels.search(query="crypto", country="RU", limit=5)

        print("Найдено в текущей выборке:", response.count)
        for channel in response.items:
            print(channel.id, channel.title, channel.username, channel.participants_count)


if __name__ == "__main__":
    asyncio.run(main())
