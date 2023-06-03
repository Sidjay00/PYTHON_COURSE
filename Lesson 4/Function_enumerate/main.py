"""
Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор 
с кортежами из индекса и элементов входных данных
Пример:
"""

# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)