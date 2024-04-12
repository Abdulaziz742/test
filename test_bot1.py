
import telebot
import sqlite3

token = '7170869812:AAF48HaHQNLBW-6aWkBOGQy5dI_E0Sev780'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('test_bot2.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER name varchar(50), password varchar(50));''')


    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Username kriting')

    bot.register_next_step_handler(message, user_name)
