from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from config.logging_admin import loger

from app.database.repository import db

from app.admin.keyboards import *
from app.admin.state_fms import StateFmsAdmin

router = Router()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    pass