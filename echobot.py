import telebot
import datetime
import pytz

# Создаем экземпляр бота
bot = telebot.TeleBot('6509664778:AAHlQofbA0dxV_uv7FUYUCxQW4-tvH9yQV0')

def get_time_of_day():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_timezone).time()
    current_hour = current_time.hour
    if 6 <= current_hour < 14:
        return "Доброе утро!"
    elif 14 <= current_hour < 19:
        return "Добрый день!"
    elif 19 <= current_hour < 24 or 0 <= current_hour < 1:
        return "Добрый вечер!"
    else:
        return "Спи давай!"
    

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    greeting = f"Машунь! {get_time_of_day()}"
    bot.send_message(m.chat.id, greeting)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Я тебя люблю :)')

@bot.message_handler(content_types=["photo"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Оооооо. Ты самая красивая ❤️')

# Запускаем бота
bot.polling(none_stop=True, interval=0)
