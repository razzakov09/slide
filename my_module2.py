# Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py".
# А затем импортируйте my_module.py в другой файл.
# import my_module


# Вам дан список имён names
# и вытащите 4 рандомных имени оттуда и сохраните в другой список.
# from random import choice
# names = [
#     "Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat",
#     "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] 
# new_names = [choice(names) for i in range(4)]
# print(new_names)


# Узнайте какая у вас операционная система с помощью модуля sys
# и выведите на экран имя опрационной системы.
# import sys
# print(sys.platform)


# Через терминал передайте Python несколько аргументов, а затем выведите их на экран.
# import sys
# text = sys.stdin.readline()
# sys.stdout.write(text)


# Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
# import os
# from random import randint
# from os import system
# for i in range(5):
#     r = randint(1, 10)
#     system(f'touch /home/avtandil/Рабочий стол{r}.txt')


# Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
# from random import choice
# names = [
#     "Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
#     "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan"] 

# def create_team(cnt_participants, cnt_team):
#     cnt_person_in_team = int(len(cnt_participants) / cnt_team)
#     res_team = []
#     for i in range(cnt_team):
#         team = []
#         for i in range(cnt_person_in_team):
#             temp = choice(names)
#             team += [temp]
#             names.remove(temp)
#         res_team.append(team)
#     return res_team
# print(create_team(names, 4))


# Напишите программу которая будет принимать аргументы sys.argv
# и выводить на экран оттуда всё что передал пользователь.
# import sys
# print("1-Аргумент", "2-Аргумент", sys.argv[0])


# Спросите у пользователя 2 значения через input() а затем через 
# модуль sys проверьте какое из 2-х значений занимает больше памяти.
# import sys
# f_val, s_val = input("First value: "), input("Second value: ")
# if sys.getsizeof(f_val) > sys.getsizeof(s_val):
#     print("First value is bigger")
# else:
#     print("Second value is bigger")


# Создайте программу которая спрашивает у пользователя число N для
# генерации пароля а затем генерирует ему пароль длиною N символов.
# import random
# import string
# def generate_random_symbols(len_of_char):
#     letters = string.ascii_lowercase
#     rand_symbols = ''.join(random.choice(letters) for i in range(len_of_char))
#     return rand_symbols
# n = int(input("input n: "))
# print(generate_random_symbols(n))


# Создайте игру Камень-Ножницы-Бумага с Компьютером. 
# Где компьютер даёт вам выбрать опцию, а сам затем генерирует
# своё значение. По итогу говорит выиграли вы, проиграли или ничья.
# from random import randint
# my_list = ['0.Камень', '1.Ножницы', '2.Бумага']
# for i in my_list: print(i)
# x, ran_x = int(input("Выберите номер опции: ")), randint(0, len(my_list)-1)
# if x == 0 and ran_x == 0 or x == 1 and ran_x == 1 or x == 2 and ran_x == 2:
#     print("ничья")
# elif x == 0 and ran_x == 1 or x == 1 and ran_x == 2 or x == 2 and ran_x == 0:
#     print("Вы выиграли")
# else:
#     print("Вы проиграли")


# Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12.
# Также получите число кратное пяти в пределах от 5 до 100.
# from random import randrange
# print(randrange(6, 12, 2))
# print(randrange(5, 100, 5))


# Найдите модуль os и sys в google и поработайте с каждым отдельно
# import os, sys
# print(os.name)
# print(sys.exc_info)


# Определить дату, которая наступит через 1000 дней от текущей даты
# import datetime
# dt = datetime.datetime.now()
# thdt = datetime.timedelta(days=1000)
# print(dt+thdt)


# Задание 1:
# С помощью цикла пройдите по листу numbers и выводите на экран сумму двух соседних чисел.
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# i, j = 0, 1
# while j != len(numbers)-1:
#     print(numbers[i] + numbers[j])
#     i += 1
#     j += 1


# Задание 2:
# В Python есть модуль datetime а в модуле есть особенные функции которые
# показывают настоящее время.
# С помощью модуля datetime выведите на экран сколько времени в данный момент.
# import datetime
# print(datetime.datetime.now())


# Задание 3:
# В Python есть модуль time, с помощью него можно отправлять программу в СОН.
# Запустите цикл for i in range(10) и каждый шаг цикла вызывайте функцию модуля time которая заставляет программу ЗАСНУТЬ.
# import time
# for i in range(10):
#     time.sleep(1)
#     print(i)


# Задание 4:
# В Python есть ВСТРОЕННАЯ функция которая позволяет объединять ДВА списка для цикла for.
# Запустите цикл for с двумя переменными которые будут проходить по list1 и list2
# одновременно и выводите эти переменные на экран.
# list1 = [1,3,5,7,9,11,13]
# list2 = [2,4,6,8,10,12,14]
# for i, j in zip(list1, list2):
#     print(i, j)