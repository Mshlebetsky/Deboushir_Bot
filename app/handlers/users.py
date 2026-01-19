from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from app.config import CHANNEL_ID, ADMIN_IDS
from app.db.orm_query import get_or_create_user, create_post, get_post_by_message_id
from app.keyboards.users import start_inline_kb, propose_kb
from app.keyboards.admins import is_channel_admin
from app.logic.states import ProposePost
from app.templates.text import welcome_text, propose_text, propose_text_to_bonya

router = Router()

@router.message(Command("start"))
async def start(message: Message, bot):
    is_admin = await is_channel_admin(bot, message.from_user.id)
    get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.full_name
    )
    await message.answer(
        welcome_text,
        reply_markup=start_inline_kb(is_admin)
    )

@router.callback_query(F.data == "start")
async def start_callback(call: CallbackQuery, bot):
    is_admin = await is_channel_admin(bot, call.message.from_user.id)
    await call.message.answer(
        welcome_text,
        reply_markup=start_inline_kb(is_admin)
    )



@router.callback_query(F.data == "propose_post")
async def propose_post(call: CallbackQuery, state : FSMContext):
    user_tag = call.from_user.username
    user_id = call.from_user.id
    # admin_tags = ["hhxxhhxxh", "bananquee"]
    if user_id in ADMIN_IDS:
        await call.message.answer(f"{propose_text_to_bonya}\n{user_id}", reply_markup=propose_kb())
    else:
        await call.message.answer(f"{propose_text}\n{user_id}", reply_markup=propose_kb())

    await state.set_state(ProposePost.waiting_for_post)


@router.callback_query(F.data == "cancel_post")
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.clear()
    is_admin = call.from_user.id in ADMIN_IDS
    await call.message.answer("❌ Предложка отменена", reply_markup=start_inline_kb(is_admin))



@router.message(ProposePost.waiting_for_post)
async def receive_post(message: Message, state: FSMContext, bot):
    create_post(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        message_id=message.message_id
    )
    is_admin = await is_channel_admin(bot, message.from_user.id)

    await message.answer("✅ Пост отправлен на модерацию", reply_markup=start_inline_kb(is_admin))
    await state.clear()
