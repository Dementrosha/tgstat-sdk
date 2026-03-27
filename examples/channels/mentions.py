import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — упоминания канала в других каналах.
        response = await client.channels.mentions(channel_id="@durov", limit=5, extended=True)

        for item in response.items:
            print("Mention ID:", item.mention_id)
            print("Тип:",        item.mention_type)
            print("Post ID:",    item.post_id)
            print("Ссылка:",     item.post_link)
            print("Дата:",       item.post_date)
            print("Channel ID:", item.channel_id)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())
