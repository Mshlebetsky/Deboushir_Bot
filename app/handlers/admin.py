from aiogram import Router, F
from aiogram.types import CallbackQuery
from app.config import CHANNEL_ID

router = Router()

@router.callback_query(F.data.startswith("approve:"))
async def approve(callback: CallbackQuery):
    await callback.message.copy_to(CHANNEL_ID)
    await callback.message.edit_caption(
        callback.message.caption + "\n\n✅ Опубликовано"
    )
    await callback.answer("Опубликовано")


@router.callback_query(F.data.startswith("reject:"))
async def reject(callback: CallbackQuery):
    await callback.message.edit_caption(
        callback.message.caption + "\n\n❌ Отклонено"
    )
    await callback.answer("Отклонено")
