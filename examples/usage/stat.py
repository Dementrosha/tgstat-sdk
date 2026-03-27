import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — список активных тарифов и квот.
        response = await client.usage.stat()

        for item in response:
            print("Тариф:",       item.title)
            print("Ключ тарифа:", item.service_key)
            print("Запросы:",     item.spent_requests)
            print("Каналы:",      item.spent_channels)
            print("Слова:",       item.spent_words)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())

