import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        # response — состояние callback URL и очереди уведомлений.
        response = await client.callback.get_callback_info()
        info = response

        print("URL:",                   info.url)
        print("Сообщений в очереди:",   info.pending_update_count)
        print("Дата последней ошибки:", info.last_error_date)
        print("Последняя ошибка:",      info.last_error_message)


if __name__ == "__main__":
    asyncio.run(main())

