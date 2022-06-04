# Создайте функцию которая которая берёт лист делит его пополам и обе стороны
# разворачивает в противоположную сторону. 
# Пример: Оригинальный Лист: list_1 = ['name', 'age', '1', '19']
# Изменённый Лист: list_1 = ['age', 'name', '19', '1']

# list_1 = ['name', 'age', '1', '19']
# def reverse_list(l):
#     f_part = l[:len(l) // 2][::-1]
#     s_part = l[len(l) // 2 :: ][::-1]
#     return f_part + s_part

# print(reverse_list(list_1))

# Создайте с помощью рекурсии функцию которая генерирует 10 чисел 
# Фибоначчи: 1,1,2,3,5,8,13,21,34,..

# fib_list = []
# def fib(n):
#     if n < 2:
#         return n
#     fib_list.append(n - 1 + n - 2)
#     return fib(n - 1) + fib(n - 2)

# print(fib(12))
# print(fib_list)


# 3. Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

# def plus_nums(n1, n2):
#     return n1+n2

# def minus_nums(n1, n2):
#     return n1-n2

# def res_func(a, b):
#     print(plus_nums(a, b))
#     print(minus_nums(a, b))

# res_func(2, 2)

# Спросите у пользователя имя файла. Создайте функцию которая 
# создаёт файл с именем которое передал пользователь. Присвойте 
# ИМЯ функции к переменной и вызывайте функцию через переменную.

# name_of_file = input("Название файла: ")

# def create_file(name_file):
#     f = open(name_file, 'w')
#     f.close()

# test = create_file(name_of_file)


# Представьте Вы работаете в Мобильной Компании и вас попросили создать генератор номеров.
# Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444 _ _ _ _ _ _.
# Номера которые вы можете генерировать могут содержать в себе только числа 145790. 
# Пример: 0444150971 0444111777 0444457901

# from random import choice

# def gen_number():
#     allow_nums = '145790'
#     res_nums = '0444'
#     for i in range(6):
#         res_nums += choice(allow_nums)
#     return res_nums

# print(gen_number())


# Напишите программу которая выводит только нечётные числа с помощью рекурсии

# def print_odd_nums(n):
#     print(n)
#     if n < 1:
#         return None
#     if n % 2 == 0:
#         return print_odd_nums(n - 2)
#     else:
#         return print_odd_nums(n - 1)

# print(print_odd_nums(7))


# Напишите функцию которая принимает SET и рекурсивно
# удаляет оттуда по одному элементу при запуске.

# my_nums = {1, 2, 3, 4, 5}
# def del_set_item(user_nums):
#     my_nums.pop()
#     return my_nums

# print(my_nums)
# print(del_set_item(my_nums))
# print(del_set_item(my_nums))
# print(del_set_item(my_nums))

