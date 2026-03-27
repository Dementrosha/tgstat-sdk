import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # Метод ставит канал в очередь на добавление и обычно возвращает status=pending.
        response = await client.channels.add(
            channel_name="@example_channel",
            country="RU",
            language="russian",
        )
        print("Статус:", response.status)


if __name__ == "__main__":
    asyncio.run(main())
