from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.config import CHANNEL_ID
from app.db.orm_query import set_post_status, get_pending_post
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.keyboards.admins import is_channel_admin, approve_post_kb, next_propose_kb, back_to_main
from app.logic.helper import publish_post_with_nickname

router = Router()


@router.callback_query(F.data == "admin_panel_show")
async def show_post(call: CallbackQuery, bot):
    is_admin = await is_channel_admin(bot, call.message.from_user.id)
    if not is_admin:
        return

    post = get_pending_post()

    if not post:
        await call.message.answer("📭 Нет постов на модерации", reply_markup=back_to_main())
        return

    await bot.copy_message(
        chat_id=call.message.chat.id,
        from_chat_id=post.chat_id,
        message_id=post.message_id,
    )
    await call.message.answer("Выберите действие", reply_markup=approve_post_kb(post.id))

@router.callback_query(F.data.startswith("approve:"))
async def approve_post(call: CallbackQuery, bot):
    post_id = int(call.data.split(":")[1])
    post = set_post_status(post_id, True)  # здесь возвращай объект Posts вместе с user

    # Публикация с никнеймом
    await publish_post_with_nickname(bot, post)

    await call.message.edit_text("✅ Пост опубликован", reply_markup=next_propose_kb())
    await call.answer("Опубликовано")





@router.callback_query(F.data.startswith("reject:"))
async def reject_post(call: CallbackQuery):
    post_id = int(call.data.split(":")[1])
    set_post_status(post_id, False)

    await call.message.edit_text("❌ Пост отклонён",reply_markup=next_propose_kb())
    await call.answer("Отклонено")