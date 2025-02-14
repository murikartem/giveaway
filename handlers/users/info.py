from aiogram.types import Message
from loader import router
from aiogram import F
import json
from random import shuffle

#with open('data/info.txt', 'r', encoding='utf-8') as file:
#    data1 = json.loads(file.read())

@router.message(F.text =='information')
async def info_start(message: Message):
    await message.answer(text='приветствую, принимай участия в конкурсе и выйграй автомобиль')