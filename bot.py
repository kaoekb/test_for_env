import telebot
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Обработчик команды /start или /help"""
    bot.reply_to(message, "Привет! Я простой эхо-бот.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    """Функция обработки сообщения и отправки обратно того же сообщения"""
    bot.reply_to(message, f"Вы сказали: {message.text}")

bot.polling()

