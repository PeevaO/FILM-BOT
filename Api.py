"""@package docstring
Documentation for this module.

Телеграм бот реализован с помощью библиотеки telebot, позволяющей работать с Telegram Bot API.
Для работы с базой данных используется библиотека sqlite3, позволяющая формировать запросы к облегченной базе данных.

Работа бота осуществляется классом DoranimeBot и сопутствующими функциями для работы с базой данных, для обращения к API Кинопоиска.
Для удобства использования добавлены кнопки в основное меню.
Запуск бота осуществляется с помощью файла "Main.py".
"""
# @section author_doxygen_example Author(s)
#Created by:
# * Pustovalova Sofya Alekseevna \n
# * Zavyalova Polina Igorevna \n
# * Peeva Olesya Romanovna \n
# * Kramarenko Yuri Andreevich \n
#on 16/06/2024.

# Imports
import requests
import textwrap


API = 'EXJ45X6-NF9MGN7-JA5CJJQ-M14FMA9'  # введите свой токен (ссылка для получения: https://kinopoisk.dev/)
URL = 'https://api.kinopoisk.dev/v1.4/'


def genre_search(message, type):
    """function for searching by genre.

    :param message: user's message
    :param type: anime or dorama
    :return: result (anime or dorama)
    """

    message = ''.join(message.split())
    genres = message.split(",")

    headers = {'X-API-KEY': API}
    if type == 'аниме':
        params = {
            'notNullFields': ['name', 'description'],
            'type': ['anime'],
            'genres.name': genres
        }
    else:
        params = {
            'notNullFields': ['name', 'description'],
            'type': ['tv-series'],
            'countries.name': ['Корея Южная', 'Япония', 'Китай'],
            'genres.name': genres
        }
    response = requests.get(URL + 'movie', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['docs']
        result = ''
        for i in range(len(data)):
            name = data[i]['name']
            description = data[i]['description']
            year = data[i]['year']
            result += f'{i+1}. {name}, {year} \n {textwrap.fill(description, 100)} \n'
    else:
        print('Не удалось подключиться:(')

    return result


def title_search(message):
    """function for searching by name.

    :param message: user's message
    :return: result (anime or dorama)
    """
    title = message

    headers = {'X-API-KEY': API}
    params = {
        'query': title
    }
    response = requests.get(URL + 'movie/search', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['docs'][0]
        name = data['name']
        description = data['description']
        year = data['year']
        result = f'{name}, {year} \n {textwrap.fill(description, 100)} \n'
    else:
        print('Не удалось подключиться:(')

    return result


def actor_search(message):
    """function for searching by actor.

    :param message: user's message
    :return: result (anime or dorama)
    """
    result = ''
    message.replace(', ', ',')
    actor = message.split(",")

    headers = {'X-API-KEY': API}

    params = {
        'query': actor
    }
    response = requests.get(URL + 'person/search', headers=headers, params=params)

    if response.status_code == 200:
        actor_id = response.json()['docs'][0]['id']
    else:
        print('Не удалось подключиться:(')

    params = {'notNullFields': ['description'],
              'type': ['tv-series'],
              'countries.name': ['Корея Южная', 'Япония', 'Китай']
              }

    response = requests.get(f'{URL}movie?page=1&limit=10&persons.id={actor_id}', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['docs']
        result = ''
        for i in range(len(data)):
            name = data[i]['name']
            year = data[i]['year']
            description = data[i]['description']
            result += f'{i + 1}. {name}, {year} \n {textwrap.fill(description, 100)} \n'
    else:
        print('Не удалось подключиться:(')

    return result


def year_search(message, type):
    """function for searching by years.

        :param message: user's message
        :param type: anime or dorama
        :return: result (anime or dorama)
        """
    year = message.replace(' ', '')

    headers = {'X-API-KEY': API}
    if type == 'аниме':
        params = {
            'notNullFields': ['name', 'description'],
            'year': year,
            'type': ['anime']
        }
    else:
        params = {
            'notNullFields': ['name', 'description'],
            'year': year,
            'type': ['tv-series'],
            'countries.name': ['Корея Южная', 'Япония', 'Китай']
        }

    response = requests.get(URL + 'movie', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['docs']
        result = ''
        for i in range(len(data)):
            name = data[i]['name']
            description = data[i]['description']
            year = data[i]['year']
            result += f'{i+1}.{name}, {year} \n {textwrap.fill(description, 100)} \n'
    else:
        print('Не удалось подключиться:(')

    return result


def random_dorama(type):
    """function for searching random dorama.

        :param type: anime or dorama
        :return: result (anime or dorama)
        """
    headers = {'X-API-KEY': API}

    if type == 'аниме':
        params = {
            'notNullFields': ['name', 'description'],
            'type': ['anime']
        }
    else:
        params = {
            'notNullFields': ['name', 'description'],
            'type': ['tv-series'],
            'countries.name': ['Корея Южная', 'Япония', 'Китай']
        }

    response = requests.get(URL + 'movie/random', headers=headers, params=params)

    if response.status_code == 200:
        print('OK')
        data = response.json()
        print(data)
        name = data['name']
        description = data['description']
        year = data['year']
        result = f'{name}, {year} \n {textwrap.fill(description, 100)} \n'
    else:
        print('Не удалось подключиться:(')

    return result
