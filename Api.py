import requests
import textwrap


API = ''  # введите свой токен (ссылка для получения: https://kinopoisk.dev/)
URL = 'https://api.kinopoisk.dev/v1.4/'


# функция для поиска по жанру
def genre_search(message, type):
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


# функция для поиска по жанру
def title_search(message):
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


# функция для поиска по жанру
def actor_search(message):
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


# функция для поиска по жанру
def year_search(message, type):
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


# функция для поиска по жанру
def random_dorama(type):
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
