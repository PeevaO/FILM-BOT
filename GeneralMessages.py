import string

START_MSG = "Привет, я бот, который поможет тебе узнать все про нужную тебе дораму или аниме и по возможности даст ссылку," \
            " где его посмотреть! 😊\n" \
            "Для того, чтобы посмотреть доступные команды, введи /help"
HELP_MSG =  "Список моих возможностей: 👇\n"\
            "Поиск по названию 🔎 - найдет дораму или аниме по введенному тобой названию \n " \
            "Поиск по жанру 🎭 - выдаст список названий сериалов по конкретному жанру или жанрам" \
            "При поиске нескольких жанров я выдам тебе те сериалы, в которых присутствуют все перечисленные тобой \n" \
            "Поиск по актеру 💎 - выдаст список названий дорам по конкретному актеру или актерам" \
            "При поиске нескольких актеров я выдам тебе те дорамы, в котрых присутствуют все перечисленные тобой актеры \n" \
            "Поиск по году 🎯 - выдаст список названий сериалов по введенному году. По желанию можно задать диапазон \n" \
            "Добавить в Избранное 📝 - добавляет название сериала, которою вы бы хотели посмотреть в Избранное \n" \
            "Мой список 📜 - показывает все сериалы, которые вы добавили в Избранное \n" \
            "Удалить из Избранного 🚫 - удаляет сериал из Избранного \n" \
            "Случайный сериал 💡 - выдаст тебе случайное аниме или дораму (пользуйся, если не знаешь, что именно хочешь посмотреть)"