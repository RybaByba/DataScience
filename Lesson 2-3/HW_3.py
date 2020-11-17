# Завдання 3
# 	Створіть матрицю чисел 3х4. Заповніть її цілими числами від 0 до 10. Знайдіть:
# 		- Суму всіх чисел матриці.
# 		- Максимальний елемент.
# 		- Суму чисел в першому рядку.
# 		- Мінімальний елемент в  другому стовбці.
#       - Максимальний елемент по головній діагоналі (діагональ, що проходить через лівий верхній та правий нижній кути).

import random


def get_row(y):
    """
    Створення рядків матриці.
    :param y: вказати кількість рядків для матриці
    :return: повертає список  для кожного рядка
    """
    row = []
    for i in range(1, y + 1):
        row.append(random.randint(0, 10))
    return row


def get_matr(x, y):
    """
    Створення матриці.
    :param x: кількість стовпчиків матриці
    :param y: кількість рядків матриці
    :return: повертає список у вигляді елементів матриці(рядки) та стовпців
    """
    matr = []
    for i in range(1, x + 1):
        matr.append(get_row(y))
    return matr


matr = get_matr(3, 3)

all_sum = sum(matr[0] + matr[1] + matr[2])


def min_elem_in_column(matrix, column_num):
    """
    Мінімальне значення у стовпчику матриці
    :param matrix: наша матриця
    :param column_num: номер стовпця, в якому требя знайти мін.елемент
    :return: повертає мін.елемент у вказаному стовпці
    """
    column = []
    for row in matrix:
        column.append(row[column_num-1])  # -1 для зручності(номер стовпчика не по індексу, а по порядковому номеру)
    return min(column)


def max_elem_in_column(matrix, column_num):
    column = []
    for row in matrix:
        column.append(row[column_num-1])
    return max(column)


def get_matrix_diagonal(matrix):
    """
    Знаходження діагоналі по мін.значеню стовпчика або рядка(для уникнення помилки)
    :param matrix: наша матриця(список з елементів)
    :return:  ...[0][0][1][1][2][2]...
    """
    print(matrix)
    diagonal = []
    rows = len(matrix)
    columns = len(matrix[0])

    for e in range(0,min(columns, rows)):
        print(f"matrix[{e}][{e}]")
        diagonal.append(matrix[e][e])

    return diagonal

cc = f"""
Our matrix is: {matr}
Suma elements in matrix: {all_sum}
Max element marix: {max(matr)}
Suma elements in row_1: {sum(matr[0])}
Min element in column_2: {min_elem_in_column(matrix=matr, column_num=2)}
Max element in column_2: {max_elem_in_column(matrix=matr, column_num=2)}
Max diagonal element: {get_matrix_diagonal(matr)}
"""

print(cc)


# Задача 4 вивести на екран n елементів ряду Фібоначі (n вводить користувач)
# 1.за допомогою цикла
# 2.за допомогою рекурсії
# 3.за допомогою формули
# 4.за допомогою матриці
#
# 1.
n = int(input('введіть число для ряду Фібоначчі'))
a = 1
b = 1
for i in range(n):
    a, b = b, a + b
    print(a)
# 2.
def fibo(n, a=1, b=1):
    if n == 0:
        exit()
    else:
        print(f"{a}")
        a, b = b, a + b
        return fibo(n-1, a, b)

print(fibo(6))
# 3.
from math import sqrt, floor


def fibo(n):
    x = (1 + sqrt(5))/2
    if n == 0:
        return 1
    else:
         print()
         return int((x**n)/sqrt(5) + 0.5)

print(fibo(7))



# Завдання 1
# 	Напишіть програму "Угадай число". Програма загадує деяке число. Користувач повинен його відгадати
# 	Приклад діалогу має мати наступний вигляд:

number = 4
name = input('введи имя >>> ')
count = 3

while count >= 1:
    print(f'{name}, вгадайте число від 1 до 10, у вас є 3 спроби >>> ')
    user_number = int(input('введіть число >>> '))
    if user_number == number:
        print('ти вгадав!')
        break
    elif user_number != number:

        if user_number > number:
            print(f'Помилка. Ваша спроба невірна. Залишилось {count} спроб. Підказака: задумане число менше \"{user_number}\" ')
        else:
            print(f'Помилка. Ваша спроба невірна. Залишилось {count} спроб.Підказака: задумане число більше \"{user_number}\"')

        print(">", count)
        if count == 1:
            print(f'{name},ти майже вгадав, але вже використав 3 спроби')

        count -= 1




