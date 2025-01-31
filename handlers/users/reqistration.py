from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, con, cursor
from aiogram import F


class Form_req(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()

@router.message(F.text =='req')
async def fun_start(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute('select * from users where id=(?)', [id_user])
    data = cursor.fetchall()
    if not data:
        await message.answer(text='Выуспешнозарегались!')