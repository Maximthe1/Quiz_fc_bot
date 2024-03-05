from aiogram import Router, F, types

from aiogram.filters import Command

from app.keyboards.main_kb import del_kb, start_kb
from app.keyboards.quest_kb import quest_1, quest_2, quest_3, quest_4, quest_5


questrt = Router()


count = 0
@questrt.message(F.text == "Начать викторину")
async def start_quiz(message: types.Message):
	await message.answer("Тема викторины 8 марта", reply_markup=del_kb)
	await message.answer("1. Кто из этих женщин первой отправился в космос?", reply_markup=quest_1)


@questrt.callback_query(F.data == "12")
async def answer_1(call: types.CallbackQuery):
	global count
	count += 1
	await call.answer("Правильно!")
	print(count)
	await call.message.answer("2. Какой цветок стал символом 8 марта - Международного женского дня?", reply_markup=quest_2)
 
 
@questrt.callback_query((F.data == "11") | (F.data == "13"))
async def answer_foll(call: types.CallbackQuery):
    await call.answer("Неправильно в следующий раз получится!")
    await call.message.answer("2. Какой цветок стал символом 8 марта - Международного женского дня?", reply_markup=quest_2)
 

@questrt.callback_query(F.data == "23")
async def answer_1(call: types.CallbackQuery):
	global count
	count += 1
	await call.answer("Правильно!")
	print(count)
	await call.message.answer("3. Какой предмет помог Мэри Поппинс передвигаться по воздуху?", reply_markup=quest_3)
 
 
@questrt.callback_query((F.data == "21") | (F.data == "22"))
async def answer_foll(call: types.CallbackQuery):
	await call.answer("Неправильно в следующий раз получится!")
	await call.message.answer("3. Какой предмет помог Мэри Поппинс передвигаться по воздуху?", reply_markup=quest_3)
 

@questrt.callback_query(F.data == "31")
async def answer_1(call: types.CallbackQuery):
	global count
	count += 1
	await call.answer("Правильно!")
	print(count)
	await call.message.answer("4. Что получал рыцарь от дамы сердца в знак особой благосклонности?", reply_markup=quest_4)
 
 
@questrt.callback_query((F.data == "32") | (F.data == "33"))
async def answer_foll(call: types.CallbackQuery):
	await call.answer("Неправильно в следующий раз получится!")
	await call.message.answer("4. Что получал рыцарь от дамы сердца в знак особой благосклонности?", reply_markup=quest_4)
 

@questrt.callback_query(F.data == "41")
async def answer_1(call: types.CallbackQuery):
	global count
	count += 1
	await call.answer("Правильно!")
	print(count)
	await call.message.answer("5. Какая из этих богинь была покровительницей брака, охраняющей мать во время родов в Древней Греции?", reply_markup=quest_5)
 
 
@questrt.callback_query((F.data == "42") | (F.data == "43"))
async def answer_foll(call: types.CallbackQuery):
	await call.answer("Неправильно в следующий раз получится!")
	await call.message.answer("5. Какая из этих богинь была покровительницей брака, охраняющей мать во время родов в Древней Греции?", reply_markup=quest_5)
 

@questrt.callback_query(F.data == "53")
async def answer_1(call: types.CallbackQuery):
	global count
	count += 1
	await call.answer("Правильно!")
	print(count)
	await call.message.answer(f"Молодец ты ответил правильно на {count}/5 вопросов", reply_markup=start_kb)
 
 
@questrt.callback_query((F.data == "52") | (F.data == "51"))
async def answer_foll(call: types.CallbackQuery):
	await call.answer("Неправильно в следующий раз получится!")
	await call.message.answer(f"Молодец ты ответил правильно на {count}/5 вопросов",reply_markup=start_kb)
 

@questrt.message(F.text == "Мои результаты")
async def results(message: types.Message):
	if count == 0:
		await message.answer(f"У вас {count} правильных ответов возможно вы  еще не прошли викторину")
	else:
		await message.answer(f"Твои результаты: {count} правильных ответов из 5", reply_markup=start_kb)