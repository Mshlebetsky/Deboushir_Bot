from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_inline_kb(is_admin: bool) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="✍️ Предложить пост",
                callback_data="propose_post"
            )
        ]
    ]
    if is_admin:
        keyboard.append([
            InlineKeyboardButton(
                text="🛠 Админ панель",
                callback_data="admin_panel_show"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def propose_kb() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                text="Отменить",
                callback_data="cancel_post"
            )
        ],
    ]


    return InlineKeyboardMarkup(inline_keyboard=keyboard)