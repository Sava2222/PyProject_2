import pyowm
import time
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('61eb1318dc4e380f99d157d0fa8652de', config_dict)
mgr = owm.weather_manager()
TG = telebot.TeleBot('5381021001:AAHTYsRIsjNGTwFX8SAwkn4-fkslrLihShE')


@TG.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "/start":
        TG.send_message(message.from_user.id, "Здравствуйте! С помощью нашего бота Вы можете узнать погоду в интересующем вас городе. Напишите пожалуйста город" + "\n")
    elif message.text.lower() == "/help":
        TG.send_message(message.from_user.id, "Напишите пожалуйста город, информацию о погоде в котором хотите получить" + "\n")
    else:
        try:
            observation = mgr.weather_at_place(message.text)
            weather = observation.weather
            temperature = round(weather.temperature('celsius')["temp"])
            temperature_fells_like = round(weather.temperature('celsius')["feels_like"])
            wind = round(weather.wind()["speed"])
            humidity = weather.humidity
            answer = "В городе " + message.text + " сейчас " + weather.detailed_status + "." + "\n"
            answer += "Температура около: " + str(temperature) + " С. Ощущается как " + str(temperature_fells_like) + " C" + "\n"
            answer += "Скорость ветра: " + str(wind) + " м/с \n"
            answer += "Влажность: " + str(humidity) + "% \n"
            answer += "Совет: "
            if temperature < -20:
                answer += "Очень холодно, одевайтесь тепло!"
            elif temperature < 0:
                answer += "Достаточно холодно, не забудьте шапку:)"
            elif temperature < 10:
                answer += "Прохладно, куртка не помешает"
            elif temperature < 20:
                answer += "Тепло, пора гулять!"
            else:
                answer += "Жарко, будьте осторожны, остерегайтесь удара!"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", answer)
        except Exception:
            answer = "Такой город не найден, пожалуйста попробуйте снова.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title(), 'Error')

        TG.send_message(message.chat.id, answer)


TG.polling(none_stop=True)
