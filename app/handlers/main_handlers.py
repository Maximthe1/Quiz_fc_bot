from aiogram import Router, F, types

from aiogram.filters import Command

from app.keyboards.main_kb import start_kb, del_kb, github


rt = Router()
# Меню 
@rt.message(Command("start"))
async def start_cmd(message: types.Message):
	await message.answer(f"Привет, {message.from_user.full_name}, я телеграмм бот - Викторина, чтобы начать викторину нажми на кнопку Начать викторину⤵️", reply_markup=start_kb)
 

@rt.message(Command("about"))
@rt.message(F.text == "О боте")
async def about(message: types.Message):
	await message.answer("Этот бот написан на языке python 3.12.1 с использованием библиотеке aiogram 3.4, исходный код данного проекта вы можете посмотреть на GitHub", reply_markup=github)
