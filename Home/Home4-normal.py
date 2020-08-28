# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
    fib1 = fib(n)
    fib2 = fib(n + 1)
    m = m - n
    if m < 2:
        quit()

    print(fib1, end=' ')
    print(fib2, end=' ')
    for i in range(2, m):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    print()
    pass
    return fib


# a = int(input('Веддите начальный элемент последовательности Фибоначчи n = '))
# b = int(input('Веддите конечный элемент последовательности Фибоначчи m = '))
# print(fibonacci(a, b))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    L_list = len(origin_list)
    for i in range(L_list):  # цикличность, выборка по длине списка (повторится N-1 раз, например длина 6 циклов 5)
        for j in range(0, L_list - i - 1):  # цикличность, выборка по индексам элементов списка
            if origin_list[j] > origin_list[j + 1]:  # сверка 1го элемента синдексом(0) со 2ым элементом с индексом (1)
                # и так 5 раз пока максимальный элемент не окажеться 6м в списке
                # после сработает внешний цикл и внутренний повторится уже 4 раза пока
                # следующий максимальный элемент кроме 6го не окажеться на 5м месте)
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
    return origin_list


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(origin_list)
res = sort_to_max(origin_list)
print(res)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# Функция filter() возвращает итератор, состоящий из тех элементов последовательности,
# для которых переданная в качестве первого аргумента функция вернула
# истину (true) или ее аналог (не ноль, не пустую строку, не None).
l1 = [-1.25, -2, 4, 5, 6]
l2 = [2, 3, 4]
poz = list(lambda x: x > 0)
poz(l1)

poz(int(list(l1)))
print(l1)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
