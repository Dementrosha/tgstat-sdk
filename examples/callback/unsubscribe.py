import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        subscriptions = await client.callback.subscriptions_list()

        if not subscriptions.subscriptions:
            print("Активных callback-подписок не найдено.")
            return

        subscription_id = subscriptions.subscriptions[0].subscription_id
        response = await client.callback.unsubscribe(subscription_id=subscription_id)

        print("Статус:", response.status)
        print("Отписка от subscription_id:", subscription_id)


if __name__ == "__main__":
    asyncio.run(main())

