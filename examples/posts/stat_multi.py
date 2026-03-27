import asyncio

from tgstat import TGStatClient

TOKEN = "paste-your-token-here"


async def main() -> None:
    async with TGStatClient(token=TOKEN) as client:
        channel_posts = await client.channels.posts(channel_id="@durov", limit=3)
        post_ids = [post.id for post in channel_posts.items]

        if not post_ids:
            print("У канала не нашлось доступных публикаций для примера.")
            return

        response = await client.posts.stat_multi(channel_id="@durov", posts_ids=post_ids)

        for item in response:
            print("Post ID:",     item.post_id)
            print("Просмотры:",   item.views_count)
            print("Репосты:",     item.shares_count)
            print("Комментарии:", item.comments_count)
            print("Реакции:",     item.reactions_count)
            print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())

