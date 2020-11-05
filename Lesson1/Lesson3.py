# colors = ['yelow', 'blue', 'red']
# print(len(colors))
# colors[-2] = 'black'   # замінити передостанній елемент на чорний
# print(colors)
# colors.pop(0)  # видалити елемент 0
# print(colors)
# colors.insert(0, 'grin')   # додати елемент в початок списку. де 0, це елемент який хочемо замінити, а grin, на який
# colors.insert(1, 'orange')
# print(colors)



# a = int(input('>>>'))
# b = int(input('>>>'))
# c = int(input('>>>'))
#
# print("сума чисел:", a+b+c)
# print("добуток чисел:", a*b*c)

# TASK 2
# number = int(input('>>>')) #найти сторону треуг.с
# number_1 = int(input('>>>'))
# c = (number**2 + number_1**2)**(1/2)
# print(c)


# TASK 3
cred = int(input('>>>'))
years = int(input('>>>'))
per = int(input('>>>'))

all_sum = cred * (per % 100)
month = years % 12
month_sum = all_sum % month
print(month_sum)