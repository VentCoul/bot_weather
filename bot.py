import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('API_KEY',
          config_dict)  # API_KEY можно взять на сайте "https://openweathermap.org/" после регистрации перейдя в соответствующий раздел
bot = telebot.TeleBot('TOKEN')  # TOKEN - ваш телеграм токен который вы получили после регистрации бота в @BotFather


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    weather_info = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
    weather_info += 'Температура: ' + str(w.temperature('celsius')['temp']) + ' градусов C' + '\n'
    weather_info += 'Максимальная температура днем: ' + str(w.temperature('celsius')['temp_max']) + ' градусов C' + '\n'
    weather_info += 'Минимальная температура: ' + str(w.temperature('celsius')['temp_min']) + ' градусов C' + '\n'
    weather_info += 'Скорость ветра: ' + str(w.wind()['speed']) + ' м/с' + '\n'
    bot.reply_to(message, weather_info)


bot.polling()
