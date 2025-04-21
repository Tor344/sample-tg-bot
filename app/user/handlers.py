from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("user"))
async def admin_panel(message: Message):
    pass