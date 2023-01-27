import telebot;
from telebot import types
bot = telebot.TeleBot('Token')
namebot = "SURVERSBot"
version = "1.0"
vk = "https://vk.com/vladkorobov"
donate = "https://www.tinkoff.ru/cf/LVZernsczy"
playlist = [
    "Топ 1 - Elley Duhé - Middle Of The Night\nТоп 2 - MELISA & TOMMO - I'm Alone\nТоп 3 - Purple Disco Machine & Sophie and the Giants - In The Dark\nТоп 4 - GAYAZOV$ BROTHER$ - МАЛИНОВАЯ ЛАДА\nТоп 5 - Imagine Dragons - Bones\nТоп 6 - Filatov & Karas & Busy Reno - Au Revoir\nТоп 7 - ETOLUBOV - Притяжение\nТоп 8 - Imanbek & BYOR - Belly Dancer\nТоп 9 - Kamazz - Как Ты Там?\nТоп 10 - David Guetta & Robin Schulz - On Repeat (Mixed)",
    "MORGENSHTERN - Cadillac\nMORGENSHTERN - El Problema\nMORGENSHTERN - Быстро\nMORGENSHTERN - РАТАТАТАТА\nMORGENSHTERN - WATAFUK?!\nMORGENSHTERN - Lollipop\nMORGENSHTERN - Новый мерин\nMORGENSHTERN - Cristal & МОЁТ\nMORGENSHTERN - ICE\nMORGENSHTERN - ПОСОСИ",
    "Тима Белорусских - Незабудка\nТима Белорусских - Витаминка\nТима Белорусских - Мокрые кроссы\nТима Белорусских - Одуванчик\nТима Белорусских - Минута вечера\nТима Белорусских - Найду тебя\nТима Белорусских - Альфа и Омега\nТима Белорусских - Я больше не напишу\nТима Белорусских - Повторим\nТима Белорусских - Алёнка",
    "Boulevard Depo - Angry toy$\nBoulevard Depo - NBA\nBoulevard Depo - Кащенко (feat. PowerpuffLuv)\nBoulevard Depo - Катафалк\nBoulevard Depo - Friendly Fire\nBoulevard Depo - DRUГ\nBoulevard Depo - DRUГ\nBoulevard Depo - OLD BLOOD\nBoulevard Depo - No Flag\nBoulevard Depo - Ни много ни мало",
    "Элджей & FEDUK - Розовое вино\nЭлджей - Рваные джинсы\nЭлджей - Hey, Guys\nЭлджей - Ультрамариновые танцы\nЭлджей - Ecstasy\nЭлджей - ZEF\nЭлджей - Ультрафиолетовая лампа\nЭлджей - Bounce\nЭлджей - Топ топ\nЭлджей - Tic-tac",
    "Макс Корж - Горы по колено\nМакс Корж - Малиновый закат\nМакс Корж - Малый повзрослел\nМакс Корж - Жить в кайф\nМакс Корж - Пьяный дождь\nМакс Корж - Небо поможет нам\nМакс Корж - Стань\nМакс Корж - Оптимист\nМакс Корж - Мотылёк\nМакс Корж - Эндорфин",
    "FACE - ROCK STAR\nFACE - PULL UP\nFACE - ДРУЖБЫ НЕ БЫВАЕТ\nFACE - ЗЕМФИРА\nFACE - МНЕ ПОХУЙ\nFACE - ИДИ НАХУЙ\nFACE - Я НОРМАЛЬНЫЙ\nFACE - ЗОЛОТО НА ШЕЕ\nFACE - ДЕСЯТЬ ПЕНСИЙ\nFACE - Я ЕБАЛ ТВОЮ ТЁЛКУ",
    "OXXXYMIRON - Восточный Мордор\nOXXXYMIRON - Город под подошвой\nOXXXYMIRON - Колыбельная\nOXXXYMIRON - Мой менталитет\nOXXXYMIRON - Неваляшка\nOXXXYMIRON - Переплетено\nOXXXYMIRON - Полигон\nOXXXYMIRON - Последний звонок\nOXXXYMIRON - Признаки жизни\nnOXXXYMIRON - Там где нас нет"
]
UpdateList = [
    "Обновление v1.0:\n- Создан Telegram bot 27.01.2023"
]
CommandList = [
    "Список команд:",
    "/help - Посмотреть список команд",
    "/start - Посмотреть каталог возможностей"
]

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "/start":
        Welcome(message, "Привет, меня зовут " + namebot + ", я помогаю с выбором музыки, например подскажу все ТОП 10 треков 2022 года, выбирай категорию, которую тебя интерисует:", True)
  
    elif message.text == "/help":
        for i in range(0, 3):
            SendBot(message, CommandList[i])

    else:
        SendBot(message, "Чтобы посмотреть список команд, введите - (/help)")

def Welcome(message, text, type):
    markup = types.InlineKeyboardMarkup()
    type1 = types.InlineKeyboardButton("Топ 10 треков 2022 года", callback_data="type1")
    type2 = types.InlineKeyboardButton("Топ 10 треков MORGENSHTERN", callback_data="type2")
    type3 = types.InlineKeyboardButton("Топ 10 треков Тима Белорусских", callback_data="type3")
    type4 = types.InlineKeyboardButton("Топ 10 треков Boulevard Depo", callback_data="type4")
    type5 = types.InlineKeyboardButton("Топ 10 треков Элджей", callback_data="type5")
    type6 = types.InlineKeyboardButton("Топ 10 треков Макс Корж", callback_data="type6")
    type7 = types.InlineKeyboardButton("Топ 10 треков FACE", callback_data="type7")
    type8 = types.InlineKeyboardButton("Топ 10 треков OXXXYMIRON", callback_data="type8")
    type9 = types.InlineKeyboardButton("Информация", callback_data="info")
    type10 = types.InlineKeyboardButton("Список обновлений", callback_data="updates")
    markup.add(type1, type2, type3, type4, type5, type6, type7, type8, type9, type10)
    if type == True:
        return bot.send_message(message.from_user.id, text, reply_markup=markup)
    bot.send_message(message, text, reply_markup=markup)

def BackMenu(message):
    markup = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton("Назад <<", callback_data="back")
    markup.add(back)
    bot.send_message(message, "Если хотите вернуться назад, нажмите кнопку \"Назад <<\"", reply_markup=markup)

def Updates(message):
    markup = types.InlineKeyboardMarkup()
    upd1 = types.InlineKeyboardButton("Обновление v1.0", callback_data="upd1")
    back = types.InlineKeyboardButton("Назад <<", callback_data="back")
    markup.add(upd1, back)
    bot.send_message(message, "Если хотите вернуться назад, нажмите кнопку \"Назад <<\"", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    match call.data:
        case "back":
            Welcome(call.message.chat.id, "Выберите категорию:", False)
        case "updates":
            Updates(call.message.chat.id)
        case "info":
            bot.send_message(call.message.chat.id, "Создатель данного бота -> " + vk + "\nПоддержать финансово данного бота -> " + donate + "\nВерсия бота: v" + version + "\nПосмотреть список обновлений можно нажав на кнопку \"Список обновлений\"")
        # -> Список обновлений
        case "upd1":
            bot.send_message(call.message.chat.id, UpdateList[0])
        # -> Категория музыки
        case "type1":
            bot.send_message(call.message.chat.id, playlist[0])
        case "type2":
            bot.send_message(call.message.chat.id, playlist[1])
        case "type3":
            bot.send_message(call.message.chat.id, playlist[2])
        case "type4":
            bot.send_message(call.message.chat.id, playlist[3])
        case "type5":
            bot.send_message(call.message.chat.id, playlist[4])
        case "type6":
            bot.send_message(call.message.chat.id, playlist[5])
        case "type7":
            bot.send_message(call.message.chat.id, playlist[6])
        case "type8":
            bot.send_message(call.message.chat.id, playlist[7])
    if call.data != "updates" and call.data != "back":
        BackMenu(call.message.chat.id)

def SendBot(message, text):
    return bot.send_message(message.from_user.id, text)

bot.polling(none_stop=True, interval=0)