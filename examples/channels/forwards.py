import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.items — репосты публикаций канала в другие каналы.
        response = await client.channels.forwards(channel_id="@durov", limit=5, extended=True)

        for item in response.items:
            print("Forward ID:", item.forward_id)
            print("Post ID:",    item.post_id)
            print("Ссылка:",     item.post_link)
            print("Дата:",       item.post_date)
            print("Channel ID:", item.channel_id)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())
