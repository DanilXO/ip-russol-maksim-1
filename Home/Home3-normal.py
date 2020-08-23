# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random  # запускаем модуль random

d = int(input(
    '(Задача №1)\n'
    '\nСколько списков желаете задать (указать числом):\n'))  # делаем запрос на количество генерируемых
# списков
n = 15  # переменная на длину списка из 15 элементов
for a in range(0, d):
    random.seed(a)  # оператор - механизм обспечения воспроизводимости результатов работы генератора случайных чисел
    m = [random.randint(-100, 100) for i in range(n)]
    import math
    c = []
    p = [i for i in m if i > 0]
    for j in p:
        x = abs(math.sqrt(j))
        if x.is_integer():
            c.append(int(x))
    print(f'Список (m) = {m}')
    if not c:
        print('Список (c) пуст, поскольку элементы исходного сгенерированного списка (m) не имеют целочисленных '
              'корней')
    else:
        print(f'Список (c) = {c}')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


# import datetime
# d = datetime.date.today()
# print (d)
#
# datetime.replace()

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
print('\n(Задача №3)\n')
m = [random.randint(-100, 100) for i in range(15)]
print(f'Список (m) = {m}')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
import random
a = [random.randint(0,15) for i in range (20)]
print(f'(Задача №4)\n'
    f'\nlst1 = {a} - исходный список')
b = []
[b.append(j) for j in a if j not in b]
for k in a:
    if k in a:
        a.remove(k)
print(f'\nlst2 = {b} - неповторяющиеся элементы исходного списка'
      f'\nlst3 = {a} - элементы исходного списка, которые не имеют повторений')