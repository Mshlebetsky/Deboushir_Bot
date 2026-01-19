from aiogram import Bot
from app.config import CHANNEL_ID

async def is_channel_admin(bot: Bot, user_id: int) -> bool:
    admins = await bot.get_chat_administrators(CHANNEL_ID)
    return any(admin.user.id == user_id for admin in admins)


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def approve_post_kb(post_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Опубликовать",
                    callback_data=f"approve:{post_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Отклонить",
                    callback_data=f"reject:{post_id}"
                )
            ]
        ]
    )

def next_propose_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="➡️ Следующий пост",
                    callback_data=f"admin_panel_show"
                ),
                InlineKeyboardButton(
                    text="🔙 Вернуться на главную",
                    callback_data=f"start"
                )
            ]
        ]
    )

def back_to_main():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 Вернуться на главную",
                    callback_data=f"start"
                )
            ]
        ]
    )