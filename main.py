import telebot
from telebot import types

bot = telebot.TeleBot('6889979361:AAEmBMtIPstVxF2UXG3tohscFuntpMCeF2U')


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	btn1 = types.KeyboardButton('1')
	btn2 = types.KeyboardButton('2')
	btn3 = types.KeyboardButton('3')
	btn4 = types.KeyboardButton('4')
	btn5 = types.KeyboardButton('5')
	markup.add(btn1, btn2, btn3, btn4, btn5)
	send_mess = f"<b>Привет {message.from_user.first_name} </b>!\nПоздравляю тебя с днем всех влюбленных❤️, и поэтому приготовил несколько задач, проходя поэтапно ты соберешь кодовое слово, назвав которое мне вживую и после этого поцеловав😚 - получишь сюрприз😏"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()

	if get_message_bot == "1":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Посмотреть первую задачу", url="https://avatars.mds.yandex.net/i?id=1b7debcd0c02de691051c8ef43f57f301379f1e0-8699590-images-thumbs&n=13"))
		final_message = "Думаю ты с ней легко справишься"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "август":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=2yTO9kgo9rI"))
		final_message = "Умничка! Я даже не сомневался что ты справишься"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "2":
		fun_message = "Продолжи фразу: моя прекрасная июльская ..."
		bot.send_message(message.chat.id, fun_message)

	elif get_message_bot == "лилия":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=Iikbs1l8bKM"))
		final_message = "Абсолютно верно, моя прекрасная июльская Лилия)"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "3":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("Третья задача", url="https://ru.pinterest.com/pin/1023161609081617036/sent/?invite_code=78554fca4e6b40d4b7b2a0bcd3558c00&sender=1023161746501828083&sfo=1"))
		final_message = "Что же там иозображено...."
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "кикяу":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=vgyNq9z8VKI"))
		final_message = "Конечно же это наша Кикуля)"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "кики":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=vgyNq9z8VKI"))
		final_message = "Конечно же это наша пушистая булочка)"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "дочка":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=vgyNq9z8VKI"))
		final_message = "Конечно же это наша доченька)"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "сладкая булочка":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("❤️", url="https://www.youtube.com/watch?v=vgyNq9z8VKI"))
		final_message = "Конечно же это наша сладкая булочка)"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

	elif get_message_bot == "4":
		fun_message = "Напиши мужу в телеграме и он отправит тебе видео❤️"
		bot.send_message(message.chat.id, fun_message)

	elif get_message_bot == "5":
		fun_message = "Мы друг друга очень любим, вместе мы родные люди. Друг без друга нам нельзя потому, что мы..."
		bot.send_message(message.chat.id, fun_message)

	elif get_message_bot == "семья":
		markup = types.InlineKeyboardMarkup()
		markup.add(types.InlineKeyboardButton("*тык*", url="https://www.youtube.com/watch?v=mg16VQULoFU"))
		final_message = "Ты сказала слово семья?..."
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
		bot.send_message(message.chat.id, "Поздравляю ты справилась со всеми задачами, кодовое слово мужу - Сеня")

	# Здесь различные дополнительные проверки и условия
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('1')
		btn2 = types.KeyboardButton('2')
		btn3 = types.KeyboardButton('3')
		btn4 = types.KeyboardButton('4')
		btn5 = types.KeyboardButton('5')
		markup.add(btn1, btn2, btn3, btn4, btn5)
		final_message = "Так, так, так\nПостой, давай попробуем еще раз, но иначе"
		bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)
