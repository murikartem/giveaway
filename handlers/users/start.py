from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, con, cursor


@router.message(Command('start'))
async def fun_start(message: Message):
    builder = ReplyKeyboardBuilder()
    for button in kb_start:
        builder.add(button)

    await message.answer(text='Добро пожаловать!',
                         reply_markup=builder.as_markup(resize_keyboard=True))