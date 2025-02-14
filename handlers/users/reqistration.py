#регистрация
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types


from loader import router, con, cursor
from aiogram import F


class Form_req(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()

@router.message(F.text =='registration')
async def fun_start(message: Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute('select * from users where id=(?)', [id_user])
    data = cursor.fetchall()
    cursor.execute('select * from status')
    data2 = cursor.fetchall()
    checker=('1',)
    if checker == data2[0]:
        if not data:
            await state.set_state((Form_req.fio))
            await message.answer(text='ДляначалавведитеФИО!',reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer(text='Выужезарегистрировались!')
    else:
        await message.answer(text='регистрациязакончена!')


@router.message(Form_req.fio)
async def get_fio(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await state.set_state(Form_req.age)
    await message.answer('а теперь введи свой возраст')

@router.message(Form_req.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form_req.numbers)
    await message.answer('а теперь введи свой номер')

@router.message(Form_req.numbers)
async def get_numbers(message: Message, state: FSMContext):
    await state.update_data(numbers=message.text)
    await state.set_state(Form_req.email)
    await message.answer('а теперь введи свой эл. почту')

@router.message(Form_req.email)
async def get_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data1 = await state.get_data()
    fio = data1['fio']
    age = data1['age']
    numbers = data1['numbers']
    email = data1['email']
    id_user = message.chat.id
    await state.clear()
    cursor.execute('insert into users (id, FIO, numbers, email, age) values (?,?,?,?,?)', [id_user, fio, numbers, email, age])
    con.commit()
    await message.answer('регистрация завершена')

