# WeatherSavaBot
# Инструкции по конфигурации и установке (Истинный путь):
Установить Python https://www.python.org/downloads/
Установить pyowm (В командной строке от имени администратора вводим: "pip install pyowm" без кавычек)
Установить pyTelegramBotAPI ("pip install pyTelegramBotAPI")
Регистрируемся на сайте погоды https://openweathermap.org/, получаем ключ API
Получаем токен и создаем нового бота через @BotFather в телеграме коммандой "/newbot"
Регистрируемся на Heroku.com и следуем мануалу, устанавливаем все что нужно.
Добавляем файл Procfile
Содержимое Procfile: worker: python weather_telegram_bot.py
Добавляем файл requirements.txt с необходимыми зависимостями и runtime.txt с версией питона.
git init
git add .
git commit -m "first commit"
heroku login
heroku create weathersavabot
git remote -v
git push heroku master
heroku ps:scale worker=1
Если надо остановить бота
heroku ps:scale worker=0
Таким образом осуществляется хостинг, но у меня по непонятной причине не получилось, если есть такая возможность, хотел бы понять почему.
Сам бот работает корректно при запуске через PyCharm. Он знает команды /start и /help выдающие вспомогательные сообщения для пользователя. При вводе города, если сайт owm предоставляет по нему информацию выводит температуру, ощущаемую температуру, облачность, скорость ветра и влажность, а также совет от автора:) Если такого города на сайте openweathermap нет, то выводится соответсвующее сообщение.
