# def our_filter(func, numbers):
#     return(el for el in numbers if func(el))

# numbers = [1, 14, 6, 10, 3, 2, 5]

# # print(list(filter(lambda x: x > 5, numbers)))

# print(list(our_filter(lambda x: x > 5, numbers)))

"""
Задача 2. Создайте метод, позволяющий замерить время работы других методов.
"""
# import time

# def stopwatch(func):
#     def decorator():
#         start_time = time.time()
#         func()
#         print(f'время выполнения {time.time() - start_time}')
#     return decorator

# @stopwatch
# def our_math_str():
#     # start_time = time.time()
#     num = '132'
#     result = int(num) + int(num*2) + int(num*3)
#     print(result)
#     # print(f'время выполнения {time.time() - start_time}')

# @stopwatch
# def our_math_int():
#     # start_time = time.time()
#     num = 132
#     result = num + num*1000 + num + num*1000000 + num*1000 + num
#     print(result)
#     # print(f'время выполнения {time.time() - start_time}')


# our_math_str()
# our_math_int()

"""
Задача 3. Создайте декоратор для метода нахождения суммы.
"""

# def print_b(func):
#     def decorator(*args):
#         # print(f'Сумма чисел {a} и {b} равна: ', end = '')
#         print(f'Сумма чисел ', end = '')        
#         for arg in args:
#             print(f'{arg} и ', end = '')
#         print('\b\bравна: ', end = '')
#         func(*args)
#     return decorator

# @print_b
# def sum(a, b):
#     print(a + b)

# @print_b
# def sum4(a, b, c, d):
#     print(a + b + c + d)

# sum(3, 5)
# sum4(4, 6, 1, 0)

"""
Задача 4. Создайте декоратор с параметрами.
"""

def greeting(hello):
    

def get_name():
    return input('Как тебя зовут? \n')

get_name()