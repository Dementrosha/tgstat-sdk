import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response.subscription_id — идентификатор callback-подписки.
        response = await client.callback.subscribe_channel(
            channel_id="@durov",
            event_types=["new_post", "edit_post"],
        )
        print("ID подписки:", response.subscription_id)


if __name__ == "__main__":
    asyncio.run(main())

