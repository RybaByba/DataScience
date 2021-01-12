# Завдання на урок:
# 1. Отримати перелік всіх книг (Автор, назва, рейтинг, рік, ціна)
# 2. Записати інформацію в базу даних (створити таблицю в sqlite)
# 3. Написати скріпт, що зберігатиме палітурку книги на компютер


from bs4 import BeautifulSoup
import requests

all_books = {}
i = 1  # ключ у словнику {1: {значення для ключа 1}}
resp = requests.get('https://nashformat.ua/catalog/top-30-knyzhok-2017-roku')
soup = BeautifulSoup(resp.text, 'html.parser')
all_info = soup.find_all('div', class_='product-list_content')  # вся інформація про кожну книгу згрупована в даному класі за домпомогою div
print(all_info[0])  # інфо про першу книгу на сайті

for el in all_info:
    author = el.find('h4').text.lstrip('/n').lstrip().rstrip()  # lstrip('/n') - видалити переніс на нову строку, lstrip() - видалити усі пробіли зліва, rstrip() - зправа
    title = el.find(class_='h3').get('title')  # або el.find('a', class_='h3').get('title')
    rating_tag = el.find('div', class_='product_rating_js').find_all('span')[2].text  # знаходимо клас рейтингу і обираємо текст 3-го 'span' -  find_all('span')[2].text
    # print(rating_tag)
    rating = float(rating_tag.lstrip('Рейтинг: '))  # видяляємо все з лівої сторони, окрім значення, яке відображаємо як float
    publication_year_tag = el.find('div', class_='row product-list_features').find_all('span')[0].text
    # print(publication_year_tag)
    publication_year = int(publication_year_tag.lstrip('Рік видання: '))
    price = float(el.find('span', class_='cost-count').text)
    link = el.find('a', class_='h3').get('href')
    all_books[i] = {'title': title, 'author': author, 'rating': rating,
                    'publik_year': publication_year, 'price': price, 'link': link}
    i += 1
print(all_books[1]['title'])
print(all_books.items())



import sqlite3

# Створити таблицю в SQL
conn = sqlite3.connect('TOP_30_books.db')
curs = conn.cursor()
sql_text = """
CREATE TABLE Books  (
                    author TEXT NOT NULL,
                    title TEXT NOT NULL,
                    rating REAL NOT NULL,
                    publik_year INTEGER NOT NULL,
                    price REAL NOT NULL,
                    link TEXT NOT NULL
                    )

"""
# curs.execute(sql_text)
# conn.close()

# Внести дані в створену таблицю
# conn = sqlite3.connect('TOP_30_books.db')
# curs = conn.cursor()
# insert_table = """
# INSERT INTO Books (author, title, rating, publik_year, price, link) VALUES (?,?,?,?,?,?)
# """
# # за допомогою функції заповнюємо в таблиці Books_TOP усі ячейки
# for elem in all_books.items():  # elem в списку словників
#     current_elem = elem[1]  # значення для поточного ключа в словнику
#     curs.execute(insert_table, (current_elem['author'],
#                                 current_elem['title'],
#                                 current_elem['rating'],
#                                 current_elem['publik_year'],
#                                 current_elem['price'],
#                                 current_elem['link'])
#                  )
# conn.commit()
# conn.close()

# Вивести назви усіх книжок. Коористувачу необхідно ввести цифру книги та зберегти її палітурку у jpeg
conn = sqlite3.connect('TOP_30_books.db')
curs = conn.cursor()

sql_get_books = '''
    SELECT title, author FROM Books
'''

books_and_authors = curs.execute(sql_get_books).fetchall()  # список кортежкей з рядків таблиці з назвою книги та автора(номер, назва, автор)
print('>>>>>>>>', books_and_authors)

i = 1

for el in books_and_authors:
    print(i, el[0], el[1])
    i += 1

book_number = int(input('Введіть обрану книгу: '))

book_to_search = books_and_authors[book_number - 1][0]  # оскільки в списку кортежей 1-й елемент нульвий, то потрібно вирівняти нумерацію [book_number-1], та відобразити назвзву книги [0]
print(book_to_search)

sql_found_book = """
SELECT * FROM Books
WHERE title = (?)
"""
found_book = curs.execute(sql_found_book, (book_to_search,)).fetchall()[0]
print(found_book)

print('Інформація стосовно обраної книги:\n', found_book)
conn.close()

link = 'https://nashformat.ua/' + found_book[5]  # до url додаємо 5-й елемент у кортежі (ссилка на окрему книгу)

r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')
# img = soup.find_all('a', class_="gallery fn-zoom btn-block img-block")
# print(img)
img = soup.find_all('a', class_="gallery fn-zoom btn-block img-block")[0].get('href')  # отримати силку на фото обраної книги
print(img)

r = requests.get(img)
img_binary = r.content  # response.content возвращает содержимое ответа в байтах.Содержит контекст запроса (напр., audio, image, iframe, итд.)


with open('image.jpeg', 'wb') as f:
    f.write(img_binary)


print(type(img_binary))