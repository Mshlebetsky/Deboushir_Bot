from aiogram import Router, F
from aiogram.types import Message

from app.templates.text import welcome_text
router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        welcome_text
    )


