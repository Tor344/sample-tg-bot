from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    pass