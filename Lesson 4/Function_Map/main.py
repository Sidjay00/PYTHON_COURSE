# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

"""
# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел.

data = '15 156 96 3 5 8 52 5'
# print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split())) # реализовываем то же самое, только через функцию map
print(data)
"""

"""
Задача взята из объяснения функции lambda
"""

# def select(f, col):
#     return [f(x) for x in col]
# Здесь функция select и есть функция map, поэтому далее по коду мы заменяем select на функцию map

def where(f, col):
    return [x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)