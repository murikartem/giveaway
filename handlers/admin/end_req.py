#заканчивание регистрации
from aiogram.filters import Command
from aiogram.types import Message
from loader import router, con, cursor, admin_id




@router.message(Command('end_req'))
async def req_end(message: Message):
    id_user = message.chat.id
    if id_user in admin_id:
        cursor.execute('update  status set state=2')
        con.commit()
        await message.answer(text='вы успешно закончили регистрацию')
    else:
        await message.answer(text='Нет доступа')