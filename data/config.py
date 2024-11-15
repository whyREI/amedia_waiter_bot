USER_FAV_LIMIT = 30
ARROW = '➻'
BTN_BACK = '🔙 Назад 🔙'
BTN_UPDATE = '🔄 Обновить 🔄'

START_MESSAGE = f"""
Добавь аниме в избранное и получи уведомление как только оно появится на сайте Amedia.online


{ARROW} /help - нажми, ести не нажимал
"""

HELP_MESSAGE = """
FAQ:
"""

HELP_ADD_MESSAGE = """
Как добавить аниме:
1. Открой "Последние", "Сегодня", "Расписание" или воспользуйся Поиском
2. Нажми на любое понравившееся аниме
3. Кнопка "Добавить в избранное" - то, что тебе нужно, нажимай
4. Отлично! Теперь этот тайтл у тебя в избранном. Чтобы посмотреть избранное нажми "Избранное"
5. Как только аниме появится на сайте, тебе придет уведомление
"""

DONATE_MESSAGE = """
⧼ Донат ⧽

"""

DAYS = {
    0: ('ПН', 'Понедельник'),
    1: ('ВТ', 'Вторник'),
    2: ('СР', 'Среда'),
    3: ('ЧТ', 'Четверг'),
    4: ('ПТ', 'Пятница'),
    5: ('СБ', 'Суббота'),
    6: ('ВС', 'Воскресение')
}

FIND_MSGS = {
    'default': '〔 Поиск 〕',
    'finding': '🔎 〔 Поиск 〕 🔍\n\nВведите название аниме:',
    'found': '〔 Поиск 〕\n\nНайдено',
    'cancel': '❌ 〔 Поиск 〕 ❌\n\nПоиск отменен'
}

FIND_BTNS = {
    'start': '☛ Найти аниме ☚',
    'cancel': '✘ Отмена ✘',
    'retry': '↻ Искать еще ↻',
}

NOTICE_MSG = 'Вышла {anime_seria} серия «{anime_name}»'
