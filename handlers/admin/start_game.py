#завершение розыгрыша
import json
from aiogram.filters import Command
from aiogram.types import Message
from loader import router, con, cursor, admin_id, Bot
import random


@router.message(Command('start_game'))
async def gg_start(message: Message, bot:Bot):
    id_user = message.chat.id
    if id_user in admin_id:
        cursor.execute('select * from users')
        data = cursor.fetchall()
        random.shuffle(data)
        with open('data/data.json', encoding='utf-8') as file:
            prize = json.loads(file.read())
        text = ('Розыгрыш завершён!\n'
                'Поздравляю победителей с победой\n'
                )
        for i in range(1):
            text += f'{data[i][1]} - {prize[i]}'
        for user in data:
            try:
                await bot.send_message(text=text, chat_id=user[0])
            except:
                pass
        cursor.execute('delete from users')
        con.commit()
        cursor.execute('update status set state=2')
        con.commit()
    else:
        await message.answer(text='Нет доступа')
