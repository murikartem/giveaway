from aiogram.filters import Command
from aiogram.types import Message
from loader import router, con, cursor, admin_id

status = False


@router.message(Command('start_req'))
async def fun_start(message: Message):
    global status
    id_user = message.chat.id
    cursor.execute('select * from users where id=(?)', [id_user])
    data = cursor.fetchall()
    if int(data['id']) == int(admin_id):
        status = True
        await message.answer(text='вы успешно запустили регистрацию')
    else:
        await message.answer(text='Нет доступа')


@router.message(Command('end_req'))
async def fun_start(message: Message):
    global status
    id_user = message.chat.id
    if id_user == int(admin_id):
        status = False
        await message.answer(text='вы успешно закончили регистрацию')
    else:
        await message.answer(text='Нет доступа')


