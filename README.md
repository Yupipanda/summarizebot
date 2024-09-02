<h1 align="center">summarizebot</h1>
<h3><p align="center">Шаблон рабочего новостного телеграмм бота.</p></h3>
<p>Данный телеграмм бот запускает парсеры, собирает инфу в базу данных, рандомизирует сами посты и их парсинг, и на выходе выдает вам нужное вам количество постов с заголовками и ссылками на новостную статью в вашу супергруппу в телеграмм. А также под каждым постом будет кнопка дать больше, которая использует утилиту <a href="https://github.com/Yupipanda/sumtext.git">sumtext</a> для выдачи краткого содержания статьи, которого отлично хватает для создания хорошего поста для своего телеграмм канала.</p>

Для начала работы клонируйте репозиторий самого бота:
```sh
git clone https://github.com/Yupipanda/summarizebot.git
cd summarizebot
```

<p>После клонирования репозитория настройте утилиту <a href="https://github.com/Yupipanda/sumtext.git">sumtext</a> в определенном месте. Укажите путь до данной утилиты в файле 'app/handlers.py', а также укажите в том файле свой user_id(Его можно найти в <a href="https://t.me/userinfobot">@userinfobot</a>) в строках где написанно. Дальше вам нужно указать telegram bot api от <a href="https://t.me/BotFather">@BotFather</a> в .env файле:"</p>

```python
TGTOKEN='ваш api ключ для тг бота:
```

Ну а дальше проще:
```sh
pip install -r requirements.txt
python3 main.py
```

Показ работы:
[Видео на Youtube Shorts](https://www.youtube.com/shorts/8tYzkRdUsqw?feature=share)
[Telegram Канал](https://t.me/yupipanda_channel)





