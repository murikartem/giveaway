#запуск регистрации
from aiogram.filters import Command
from aiogram.types import Message
from loader import router, con, cursor, admin_id



@router.message(Command('start_req'))
async def req_start(message: Message):
    id_user = message.chat.id
    if id_user in admin_id:
        cursor.execute('update  status set state=1')
        con.commit()
        await message.answer(text='вы успешно запустили регистрацию')
    else:
        await message.answer(text='Нет доступа')





