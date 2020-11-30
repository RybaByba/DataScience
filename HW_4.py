# Завдання 1
# easy: вивести фільми та посилання на них із першої сторінки
# medium: вивести фільми та посилання на них зі всіх сторінок
# hard:  вивести фільми, посилання та акторів зі всіх сторінок


from bs4 import BeautifulSoup
import requests
from pprint import pprint

resp = requests.get('https://sweet.tv/movies/multfilmi')
soup = BeautifulSoup(resp.text, 'html.parser')

# for link in soup.find_all(class_='film-item'):
#     print(link.get('href'))
#
# for link in soup.find_all(class_='film-item'):
#     print(link.get('title'))


films = {}


def get_films(url):
    links = {}
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    for link in soup.find_all(class_='film-item'):
        links.update({link.get('title'): link.get('href')})

    return links


pages = []

for link in soup.find_all(class_='page-link'):

    if link.get('href') is not None:
        pages.append(link.get('href'))

next_page = pages[0]
last_page = pages[-1]

next_page_number = next_page.split("/")[-1]
last_page_number = last_page.split("/")[-1]
pages_url = next_page.replace(next_page_number, "")

for page in range(int(next_page_number), int(last_page_number)):
    films.update(get_films(f"{pages_url}{page}"))


# print(f"get from page {pages_url}{page}")
# pprint(films)


def get_actors(films):
    films_data = {}
    # films = {'Принцеса і жаба': 'https://sweet.tv/movie/19873-princesa-i-zhaba'}
    # print(films)

    for film_name, film_url in films.items():
        actors = []

        r = requests.get(film_url)
        soup = BeautifulSoup(r.text, 'html.parser')

        for l in soup.find_all("p", itemprop="name"):
            actors.append(l.text)

        films_data.update({film_name: {"url": film_url, "actors": actors}})

    return films_data


pprint(get_actors(films))


# Завдання 3
# Написати скріпт, який зчитує стрічку, записує її в файл з назвою "my_module.py".
# Даний модуль потрібно потім імпортувати:
# "import my_module"

# import pickle
# my_string = 'Hello my teacher!'
#
# with open('my_module.py.pickle', 'wb') as f:
#     pickle.dump(my_string, f)
#
# with open('my_module.py.pickle', 'rb') as f:
#     my_module = pickle.load(f)
#
# print(my_module)
