from aiogram.types import Message, InputMediaPhoto, InputMediaVideo
from app.config import CHANNEL_ID

async def publish_post_with_nickname(bot, post):
    nickname = getattr(post.user, "nickname", None) or "Аноним"
    base_text = getattr(post, "text", None)

    # Если это текстовое сообщение
    if base_text:
        final_text = f"{base_text}\n\n— предложено: {nickname}"
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=final_text
        )
        return

    # Для медиа сообщений
    await bot.copy_message(
        chat_id=CHANNEL_ID,
        from_chat_id=post.chat_id,
        message_id=post.message_id,
        caption=f"— предложено: {nickname}"  # добавляем подпись
    )
