# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

"""
Задача взята из объяснения функции lambda
"""

# def where(f, col):
#     return [x for x in col if f(x)]
# Здесь функция where и есть функция filter, поэтому далее по коду мы заменяем where на функцию filter

data = [1,2,3,5,8,15,23,38]
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)