#"""1 змінити значення так, щоб значення першого елемента виявилось в значенні другого елемента,
#і навпаки""""

# a = int(input('>>>'))
# b = int(input('>>>'))
# a = b - a
# b = b - a
# a = b + a
# print(a, b)

# or
# a = int(input('>>>'))
# b = int(input('>>>'))
# a, b = b, a
# print(a, b)

# or
# a = int(input('>>>'))
# b = int(input('>>>'))
# elem = a
# a = b
# b = elem
# print(a, b)


#2 знайти добуток цифр тризначного числа
# number = (input('>>>'))
# product = 1
# all_sum = 0
#
# for i in number:
#     all_sum += int(i)
#     product *= int(i)
# print('добуток чисел = ', product, 'сума чисел = ', all_sum)

# or
# number = int(input('>>>'))
# a = number // 100
# b = (number // 10) % 10
# c = number % 10
#
# all_sum = a + b + c
# product = a * b * c
# print('добуток чисел = ', product, 'сума чисел = ', all_sum)

#3 обчислити довжину гіпотинузи по двом введеним катетем
# a = int(input('>>>'))
# b = int(input('>>>'))
# print('довжина гіпотинузи = ', ((a**2 + b**2) ** (1/2)))

#4 розрахувати місячні виплати по кредиту і сумарну суму кредиту (прості відсотки)
# credit = int(input('введіть суму кредиту >>> '))
# interest_rate = int(input('введіть відсоткову ставку кредиту >>> '))
# years = int(input('введіть кількість років >>> '))
# all_sum = round(credit * (1 + interest_rate/100 * years * 365 / 365), 2)
# print('загальна сума кредиту, з нарахованими відсотками, буде становити >>> ', all_sum)
# sum_of_months = round(all_sum / years / 12, 2)
# print('сума кредиту кожного місяця, з урахуванням відсотків, стоновитиме>>> ', sum_of_months)

#5 користувач вводить 2 букви. визначити на яких місцях алфафіту вони стоять, і скільки мідж ними знаходиться букв.
let1 = input('введіть будь-яку літеру англійського алфавіту >>> ')
let2 = input('введіть будь-яку літеру англійського алфавіту >>> ')
print('літера', let1, 'має місце в алфавіті ', ord(let1))
print('літера', let2, 'має місце в алфавіті ', ord(let2))
distance = abs((ord(let1) - ord(let2)) + 1)
print('між літерою', let1, 'та літерою', let2, 'відстань ', distance, 'символи')