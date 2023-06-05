import telebot
import requests
import time

bot = telebot.TeleBot("", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
	
@bot.message_handler(content_types=['text'])
def greeting(message):
	# print(message)
	text = message.text
	if 'привет' in text:
		bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
	elif 'погода' in text:
		req = requests.get('https://wttr.in/?0T')
		bot.reply_to(message, req.text)
	elif text == 'котик':
	    req = requests.get('https://cataas.com/cat')
	    bot.send_photo(message.chat.id, req.content)

bot.polling()