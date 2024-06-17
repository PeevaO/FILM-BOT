"""import moduls"""
import telebot
from telebot import types
import sqlite3
import GeneralMessages
from dorama_and_anime import Dorama, Anime
import Api


class DoranimeBot:
    def __init__(self, token: str):
        """initialization

        :param token: TeleBot token
        """
        self.bot = telebot.TeleBot(token)
        self.user_data = {}
        self.conn = sqlite3.connect('Serials.db', check_same_thread=False)
        self.create_tables()
        self.load_user_data()

        """Setting up commands"""
        self.bot.message_handler(commands=['start'])(self.start)
        self.bot.message_handler(commands=['help'])(self.help)
        self.bot.message_handler(content_types=['text'])(self.func)

    def start(self, message):
        """

        :param message: user's message
        :return: response to the user
        """
        chat_id = message.chat.id
        if chat_id not in self.user_data:
            self.user_data[chat_id] = {'doramas': [], 'anime': []}
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🌸 Аниме")
        btn2 = types.KeyboardButton("📺 Дорамы")
        btn3 = types.KeyboardButton("❤️ Избранное")
        btn4 = types.KeyboardButton("❓ Что я умею?")
        markup.add(btn1, btn2, btn3, btn4)
        self.bot.send_message(message.chat.id, GeneralMessages.START_MSG, reply_markup=markup)

    def help(self, message):
        self.bot.send_message(message.chat.id, GeneralMessages.HELP_MSG)

    def func(self, message):
        """Main menu

        :param message: user's message
        :return: response to the user
        """
        if (message.text == "❓ Что я умею?"):
            self.bot.send_message(message.chat.id, GeneralMessages.HELP_MSG)
        elif (message.text == "🌸 Аниме"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Поиск аниме по названию 🔎")
            btn2 = types.KeyboardButton("Поиск аниме по жанру 🎭")
            btn3 = types.KeyboardButton("Поиск аниме по году 🎯")
            btn4 = types.KeyboardButton("Случайное аниме 💡")
            back = types.KeyboardButton("Вернуться в главное меню 📌")
            markup.add(btn1, btn2, btn3, btn4, back)
            self.bot.send_message(message.chat.id, text="Вы в разделе 🌸 Аниме", reply_markup=markup)

        elif (message.text == "📺 Дорамы"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Поиск дорамы по названию 🔎")
            btn2 = types.KeyboardButton("Поиск дорамы по жанру 🎭")
            btn3 = types.KeyboardButton("Поиск дорамы по году 🎯")
            btn4 = types.KeyboardButton("Случайная дорама 💡")
            btn5 = types.KeyboardButton("Поиск дорамы по актеру 💎")
            back = types.KeyboardButton("Вернуться в главное меню 📌")
            markup.add(btn1, btn2, btn3, btn4, btn5, back)
            self.bot.send_message(message.chat.id, text="Вы в разделе 📺 Дорамы", reply_markup=markup)

        elif (message.text == "❤️ Избранное"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Мой список 📜")
            btn2 = types.KeyboardButton("Добавить в Избранное 📝")
            btn3 = types.KeyboardButton("Удалить из Избранного 🚫")
            back = types.KeyboardButton("Вернуться в главное меню 📌")
            markup.add(btn1, btn2, btn3, back)
            self.bot.send_message(message.chat.id, text="вы в разделе ❤️ Избранное", reply_markup=markup)


        elif (message.text == "Вернуться в главное меню 📌"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🌸 Аниме")
            btn2 = types.KeyboardButton("📺 Дорамы")
            btn3 = types.KeyboardButton("❤️ Избранное")
            btn4 = types.KeyboardButton("❓ Что я умею?")
            markup.add(btn1, btn2, btn3, btn4)
            self.bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

        elif (message.text == "Поиск аниме по названию 🔎"):
            msg = self.bot.send_message(message.chat.id, 'Введи название аниме, которое хочешь посмотреть')
            self.bot.register_next_step_handler(msg, self.process_title_search)

        elif (message.text == "Поиск дорамы по названию 🔎"):
            msg = self.bot.send_message(message.chat.id, 'Введи название дорамы, которую хочешь посмотреть')
            self.bot.register_next_step_handler(msg, self.process_title_search)

        elif (message.text == "Поиск аниме по жанру 🎭"):
            self.type = 'аниме'
            msg = self.bot.send_message(message.chat.id,
                                   'Введи нужные жанры (если их несколько, то укажи их через запятую, без пробелов)')
            self.bot.register_next_step_handler(msg, self.process_genre_search)

        elif (message.text == "Поиск дорамы по жанру 🎭"):
            self.type = 'дорама'
            msg = self.bot.send_message(message.chat.id,
                                   'Введи нужные жанры (если их несколько, то укажи их через запятую, без пробелов)')
            self.bot.register_next_step_handler(msg, self.process_genre_search)

        elif (message.text == "Поиск дорамы по актеру 💎"):
            msg = self.bot.send_message(message.chat.id,
                                   'Введи нужных актеров (если их несколько, то укажи их через запятую, без пробелов)')
            self.bot.register_next_step_handler(msg, self.process_actor_search)

        elif (message.text == "Поиск дорамы по году 🎯"):
            self.type = 'дорама'
            msg = self.bot.send_message(message.chat.id,
                                   'Введи нужный год или диапазон годов (если вводишь диапазон, то вводи в формате год-год)')
            self.bot.register_next_step_handler(msg, self.process_year_search)

        elif (message.text == "Поиск аниме по году 🎯"):
            self.type = 'аниме'
            msg = self.bot.send_message(message.chat.id,
                                   'Введи нужный год или диапазон годов (если вводишь диапазон, то вводи в формате год-год)')
            self.bot.register_next_step_handler(msg, self.process_year_search)

        elif (message.text == "Случайная дорама 💡"):
            type = 'дорама'
            msg = self.bot.send_message(message.chat.id, 'Держи случайную дораму, надеюсь, что тебе она понравится 😊\n')
            information = Api.random_dorama(type)
            self.bot.send_message(message.chat.id, information)

        elif (message.text == "Случайное аниме 💡"):
            type = 'аниме'
            msg = self.bot.send_message(message.chat.id, 'Держи случайное аниме, надеюсь, что тебе оно понравится 😊\n')
            information = Api.random_dorama(type)
            self.bot.send_message(message.chat.id, information)

        elif (message.text == "Добавить в Избранное 📝"):
            msg = self.bot.send_message(message.chat.id, 'Введи, что ты хочешь добавить: аниме или дораму')
            self.bot.register_next_step_handler(msg, self.add_serial)

        elif (message.text == "Мой список 📜"):
            msg = self.bot.send_message(message.chat.id, 'Введи, что ты хочешь увидеть: аниме или дорамы')
            self.bot.register_next_step_handler(msg, self.list_serial)

        elif (message.text == "Удалить из Избранного 🚫"):
            msg = self.bot.send_message(message.chat.id, 'Введи, что ты хочешь удалить: аниме или дораму')
            self.bot.register_next_step_handler(msg, self.delete_serial)


        else:
            self.bot.send_message(message.chat.id,
                             text="⚙️ На такую команду я не запрограммирован... попробуйте другую или введите /help")

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS doramas (
                            chat_id INTEGER,
                            name TEXT, 
                            comment TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS anime (
                            chat_id INTEGER,
                            name TEXT, 
                            comment TEXT)''')
        self.conn.commit()

    def load_user_data(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM doramas')
        doramas = cursor.fetchall()
        cursor.execute('SELECT * FROM anime')
        anime = cursor.fetchall()

        for chat_id, name, comments in doramas:
            if chat_id not in self.user_data:
                self.user_data[chat_id] = {'doramas': [], 'anime': []}
            self.user_data[chat_id]['doramas'].append(Dorama(name, comments))

        for chat_id, name, comments in anime:
            if chat_id not in self.user_data:
                self.user_data[chat_id] = {'doramas': [], 'anime': []}
            self.user_data[chat_id]['anime'].append(Anime(name, comments))

    def add_serial(self, message):
        """adding a dorama or anime to the database

        :param message: dorama or anime
        :return:
        """
        chat_id = message.chat.id
        serial = message.text
        msg = self.bot.reply_to(message, 'Введите название сериала, который вы хотите добавить')
        self.bot.register_next_step_handler(msg, self.process_name_serial, chat_id, serial)

    def process_name_serial(self, message, chat_id, serial):
        name = message.text
        if (serial == 'дорама') or (serial == 'дорамы'):
            self.user_data[chat_id]['current_dorama_name'] = name
        else:
            self.user_data[chat_id]['current_anime_name'] = name
        msg = self.bot.reply_to(message, 'Введите комментарии к сериалу')
        self.bot.register_next_step_handler(msg, self.process_comment_serial, chat_id, serial)

    def process_comment_serial(self, message, chat_id, serial):
        comment = message.text
        if (serial == 'дорама') or (serial == 'дорамы'):
            name = self.user_data[chat_id].pop('current_dorama_name')
            self.user_data[chat_id]['doramas'].append(Dorama(name, comment))
            self.save_serial(chat_id, name, comment, serial)
        else:
            name = self.user_data[chat_id].pop('current_anime_name')
            self.user_data[chat_id]['anime'].append(Anime(name, comment))
            self.save_serial(chat_id, name, comment, serial)
        self.bot.send_message(chat_id, f"В раздел {serial} добавлен '{name}' с комментарием: {comment}")

    def save_serial(self, chat_id, name, comment, serial):
        cursor = self.conn.cursor()
        if (serial == 'дорама') or (serial == 'дорамы'):
            cursor.execute('INSERT INTO doramas (chat_id, name, comment) VALUES (?, ?, ?)',
                           (chat_id, name, comment))
        else:
            cursor.execute('INSERT INTO anime (chat_id, name, comment) VALUES (?, ?, ?)',
                           (chat_id, name, comment))
        self.conn.commit()

    def delete_serial(self, message):
        """deleting a dorama or anime from the database

        :param message: dorama or anime
        :return:
        """
        chat_id = message.chat.id
        serial = message.text
        msg = self.bot.reply_to(message, 'Введите название сериала, который нужно удалить:')
        self.bot.register_next_step_handler(msg, self.process_delete_serial, chat_id, serial)

    def process_delete_serial(self, message, chat_id, serial):
        name = message.text
        self.user_data[chat_id]['doramas'] = [dorama for dorama in self.user_data[chat_id]['doramas'] if dorama.name != name]
        self.delete_serial_from_db(chat_id, name, serial)
        self.bot.send_message(chat_id, f'{serial} {name} удалёна')

    def delete_serial_from_db(self, chat_id, name, serial):
        cursor = self.conn.cursor()
        if (serial == 'дорама') or (serial == 'дорамы'):
            cursor.execute('DELETE FROM doramas WHERE chat_id = ? AND name = ?', (chat_id, name))
        else:
            cursor.execute('DELETE FROM anime WHERE chat_id = ? AND name = ?', (chat_id, name))
        self.conn.commit()

    def list_serial(self, message):
        """displaying a list of favorites

        :param message:
        :return:
        """
        chat_id = message.chat.id
        serial = message.text
        valid_serials = []
        if (serial == 'дорама') or (serial == 'дорамы'):
            doramas = self.user_data[chat_id]['doramas']
            self.user_data[chat_id]['doramas'] = valid_serials
            if not doramas:
                self.bot.send_message(chat_id, "Ваш список пуст 🥺")
            else:
                doramas_str = "\n".join(str(dorama) for dorama in doramas)
                self.bot.send_message(chat_id, f"Ваш список избранного 🔥:\n{doramas_str}")
        else:
            anime = self.user_data[chat_id]['anime']
            self.user_data[chat_id]['doramas'] = valid_serials
            if not anime:
                self.bot.send_message(chat_id, "Ваш список пуст 🥺")
            else:
                anime_str = "\n".join(str(anima) for anima in anime)
                self.bot.send_message(chat_id, f"Ваш список избранного 🔥:\n{anime_str}")

    def process_title_search(self, message):
        chat_id = message.chat.id
        title = message.text
        information = Api.title_search(title)
        self.bot.send_message(chat_id, information)

    def process_genre_search(self, message):
        chat_id = message.chat.id
        genre = message.text
        information = Api.genre_search(genre, self.type)
        self.bot.send_message(chat_id, information)

    def process_actor_search(self, message):
        chat_id = message.chat.id
        title = message.text
        information = Api.title_search(title)
        self.bot.send_message(chat_id, information)

    def process_year_search(self, message):
        chat_id = message.chat.id
        year = message.text
        information = Api.year_search(year, self.type)
        self.bot.send_message(chat_id, information)

    def run(self):
        self.bot.infinity_polling()
