
import telebot
import sqlite3

token = '7170869812:AAF48HaHQNLBW-6aWkBOGQy5dI_E0Sev780'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('test_bot2.db')
    cur = conn.cursor()
def hello()
    pass
def ismoil_func():
    pass

    cur.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER name varchar(50), password varchar(50));''')


    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Username kriting')

    bot.register_next_step_handler(message, user_name)


name = ''


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Paro'lni kiriting")
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    password = message.text.strip()
    conn = sqlite3.connect('test_bot.db')
    cur = conn.cursor()
    data = (f"{name}", F"{password}")
    cur.execute(f"INSERT INTO user (name, password) VALUES {data}")
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardMarkup("Userlar royxati", callblack_data="user"))
    bot.send_message(message.chat.id, "Royxatdan otildi", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call, el=None):
    conn = sqlite3.connect('test_bot.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    user = cur.fetchone()
    info = ''
    for i in user:
        info += f"ism{el[1]} Parol {el[2]}"

    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


print("The bot is running...")
bot.polling()

