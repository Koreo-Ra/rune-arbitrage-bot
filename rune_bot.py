import requests, telebot, time, json
from decimal import Decimal, ROUND_FLOOR
from telebot import types
import matplotlib.pyplot as plt
def price_difference_t():
    binance_rune_Price = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=RUNEBUSD").json()
    binance_price = float((binance_rune_Price['price']))
    pule_rune_Price = requests.get("https://midgard.thorchain.info/v2/stats").json()
    pule_price = float((pule_rune_Price["runePriceUSD"]))
    price_difference = Decimal(str(binance_price - pule_price))
    price_difference = str(price_difference.quantize(Decimal("1.00000"), ROUND_FLOOR))
    return price_difference
def draf():
	start_reading = time.time() - 7 * 24 * 60 * 60
	figure_x = []
	with open("price_info.txt", "r") as f:
		while True:
			try:
				read_line = json.loads(f.readline())
				figure_x.append(read_line["price_difference"])
			except json.decoder.JSONDecodeError:
				break
	plt.plot(figure_x)
	plt.title('Rune price', fontsize=15)
	plt.savefig('saved_figure.png')
def price(number):
	if float(number) <= -0.03:
		text = "Pule --> Binance\nPrice difference - " + number
	elif float(number) >= 0.08:
		text = "Binance --> Pule\nPrice difference - " + number
	else:
		text = "Now is not the time for arbitration\nPrice difference - " + number
	return text
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN")
@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("⏱ Time?")
	item2 = types.KeyboardButton("📈 Graph!")
	markup.add(item1, item2)
	bot.send_message(message.chat.id, "Good afternoon , {0.first_name}!\nI'm - <b>{1.first_name}</b>, created to help with arbitration".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "⏱ Time?":
			bot.send_message(message.chat.id, price(price_difference_t()))
		elif message.text == '📈 Graph!':
			draf()
			img = open('saved_figure.png', 'rb')
			bot.send_photo(message.chat.id, img)
		else:
			bot.send_message(message.chat.id, '🤨 I do not know what to do')
bot.polling(none_stop=True)