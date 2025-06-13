from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from config.logging_admin import loger

from app.database.repository import db

from app.user.keyboards import *
from app.user.state_fms import StateFmsUser


router = Router()

@router.message(Command("user"))
async def user(message: Message):
    pass