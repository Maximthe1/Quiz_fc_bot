from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



start_kb = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Начать викторину"),
		],
		[
			KeyboardButton(text="Мои результаты"),
			KeyboardButton(text="О боте")
		],	

	],
	resize_keyboard=True,
	one_time_keyboard=True
)


github = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="GitHub", url="https://github.com/Maximthe1?tab=repositories"),
		]
	]
)


del_kb = ReplyKeyboardRemove()
