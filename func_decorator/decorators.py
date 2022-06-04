# 1
# Создайте 2 функции где одна функция вложена в другую.
# Главная функция должна выводить на экран текст: "Я главная функция".
# А вложенная функция должна выводить на экран: "Я вложенная функция."

# def func1():
#     print("Я главная функция")
#     def func2():
#         print("Я вложенная функция")
#     return func2()
# func1()


# 2
# Создайте функцию которая принмает тип данных dictionary, но возвращает 
# два Tuple в одном из них все ключи, в другом только значения.

# def func_dict(**kwargs):
#     return tuple(kwargs.keys()), tuple(kwargs.values())

# print(func_dict(first = '1', second = '2'))


# 3
# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. 
# Простое число - это число которое делится только на себя и на 1

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(9))


# 4
# Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и
# возвращает их в листе. Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты 
# в первой функции и вернёт всё так же лист

# from random import randint

# def del_repeat_el(f):
#     print(f"Original: \n {f()}")
#     def decor():
#         return list(set(f()))
#     return decor

# @del_repeat_el
# def gen_list():
#     l = [randint(10, 50) for i in range(100)]
#     return l

# print(f"Updated: \n {gen_list()}")


# 5
# Напишите функцию которая спрашивает у пользователя login и password.
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные.
# (Можете воспользоваться функцией ord и char, можете загуглить...)

# def encrypt_data(f):
#     def decor():
#         login, password = f()
#         login, password = [ord(i) for i in login], [ord(i) for i in password]
#         return login, password
#     return decor

# @encrypt_data
# def registration():
#     login = input("Login: ")
#     password = input("Password: ")
#     return login, password

# print(registration())


# 6
# Создайте 4 функции: add(), substract(), multiply(), divide() которые будут принимать
# по 2 аргумента и возвращать результат: сложения, вычитания, умножения и деления.

# add = lambda a, b: a + b
# substract = lambda a, b: a - b
# multiply = lambda a, b: a * b

# def divide(a, b):
#     try: return a / b
#     except: return "Zero error"

# print(add(2,4))
# print(substract(2,4))
# print(multiply(2,4))
# print(divide(2,0))



















# def main_func(f):
#     print(f)
#     def decor(*args, **kwargs):
#         res = f(*args, **kwargs)
#         return f
#     return decor

# @main_func
# def first_func():
#     return "Я главная функция"

# @main_func
# def second_func():
#     return "Я вложенная функция"

