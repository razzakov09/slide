# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
# Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir. 
# В итоге у вас на рабочем столе должен появиться файл directories.txt. 
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

# f = open("/home/avtandil/Рабочий стол/directories.txt", 'r')
# print(f.read())
# f.close()

# Создайте файл users.txt. Напишите программу 
# которая спрашивает у 
# пользователя его Логин и Пароль и записывает в файл users.txt.

# user_login = input('Введите логин: ')
# user_passw = input('Введите пароль: ')
# f2 = open('f2.txt', 'w')
# f2.write(user_login)
# f2.write(user_passw)
# f2.close()

# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, 
# то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”.
#  Подсказка: используйте ключевое слово in.

# f3 = open("f3.txt", "w")
# f3.write("qertyukhwgjfhdgsdghjh,hgmgd")
# f3 = open("f3.txt", "r")

# if "w" in f3.read():
#     print("в тексте есть w")
# else:
#     print("в тексте нет w")
# f3.close()

# Создайте текстовый файл python.txt и запишите в него текст #1:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.

text = '''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.'''

# t_words = []
# f4 = open('python.txt', 'w')
# f4.write(text)
# f4 = open('python.txt', 'r')
# for i in f4.read().split():
#     if 't' in i or 'T' in i:
#         t_words.append(i)
# f4.close()
# print(t_words)

# Создайте database.txt файл с несколькими логинами и паролями.
# Затем попросите пользователя войти или зарегистрироваться. Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться
# спросив пароль. Если такого логина неоказалось среди уже существющих продолжайте регистрацию.
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают

# while True:
#     have_account = input("1.Войти \n2.Зарегистрироваться\n")

#     if have_account == '1':
#         user_login = input("Login: ")
#         user_pass = input("Password: ")

#         with open('database.txt', 'r') as f5:
#             if user_login == '' or user_pass == '':
#                 print("Неправильный логин или пароль")
#             elif user_login + ' ' + user_pass in f5.read():
#                 print("Добро пожаловать!")
#                 break
#             else:
#                 print("Вы не зарегистрированы!")
#     elif have_account == '2':
#         user_login = input("Login: ")
#         user_pass = input("Password: ")
#         user_pass2 = input("Repeat password: ")

#         with open('database.txt', 'r') as f5:
#             if user_pass == '' or user_pass2 == '':
#                 print('Введите поле "password"')
#             elif user_pass != user_pass2:
#                 print("Пароли не совпадают")
#             elif user_login + ' ' in f5.read():
#                 print("Аккаунт уже зарегистрирован!")
#             else:
#                 with open('database.txt', 'a') as f5:
#                     f5.write(user_login + ' ' + user_pass + "\n")
#                 print("Аккаунт успешно зарегистрирован!")
#                 break
#     else:
#         print("Выберите 1-действие или 2-действие")


# Создайте форму регистрации которая спрашивает у пользователя: Логин, Пароль и Фото. 
# Заранее подготовьте фото на компьютере и когда программа спросит ваше фото просто 
# укажите полный путь до места где лежит ваше фото. Программа должна проверить если 
# фото правда существует по такому пути И также это фото с одним из 3 расширений("jpeg", "jpg", "png")
# то вы сохраняете в файл логин, пароль, путь до фото которое указал пользователь. 
# А самому пользователю вы говорите о том что Регистрация Успешна!

# import os.path

# user_login = input("Login: ")
# user_password = input("Password: ")
# file_path = input("path to photo: ")
# list_files = []
# list_expands = []

# def expands():
#     user_expands = ['jpg', 'png', 'jpeg']
#     for i in user_expands:
#         if i in list_expands:
#             return True
#     return False

# if os.path.exists(file_path):
#     list_files = os.listdir(file_path)
#     list_expands = [i.split('.')[1] for i in list_files]
    
#     if expands():
#         with open('f4.txt', 'a') as f6:
#             f6.write(user_login + "\n" + user_password + "\n" + file_path)
#         print("Регистрация успешна!")
#     else:
#         print("Фото с такимими расширениями не существует")
# else:
#     print("Файлы не найдены")


# Напишите программу которая спрашивает от пользователя 2 вещи:
# 1.Путь до картинки которую нужно изменить.
# 2.Путь до картинки НА которую нужно изменить.
# Если оба пути существуют перепишите первую картинку на вторую, 
# если нет скажите пользователю какой картинке не существует.

# import os.path

# first_path = input("Путь до 1-картинки: ")
# second_path = input("Путь до 2-картинки: ")

# if os.path.isfile(first_path) and os.path.exists(second_path):
#     first_path, second_path = second_path, first_path
#     print(f"Путь первой картинки: {first_path}")
#     print(f"Путь второй картинки: {second_path}")
# elif os.path.isfile(first_path) == False:
#     print("1-картинки не существует")
# elif os.path.isfile(first_path) == False:
#     print("2-картинки не существует")
# else:
#     print("Фотки не найдены")


# Возьмите текст #2 и вставьте его в текстовый файл. 
# Возьмите данные из файла и сложите зарплату за Май, Июль,
# Сентябрь и Ноябрь и посчитайте среднее арифмитечское за эти месяца.

# my_list = []
# count_of_month = 0
# sum = 0

# with open("months.txt", "r") as f7:
#     my_list = [i for i in f7.readlines()]

# for i in my_list:
#     if i.split()[0] in ('May', 'July', 'September', 'November'):
#         count_of_month += 1
#         sum += int(i.split()[1])

# print(sum / count_of_month)


# Создайте текстовый файл с целыми числами ->
# Найти максимальное и минимальное число и записать в другой файл.

# with open('numbers.txt', 'w') as numbers:
#     numbers.write('1 2 3 4 5 6 7 8 9')

# with open('numbers.txt', 'r') as list_num:
#     my_list = [i for i in list_num.read().split()]

# with open('numbers2.txt', 'w') as numbers2:
#     numbers2.write(max(my_list) + " " + min(my_list))


# Создайте текстовый файл ->
# Записать в него построчно данные, которые вводит пользователь
# Окончание ввода должен принимать пустую строку

# with open('user_text.txt', 'w') as user_text:
#     user_txt = input("Введите текст: ").split()
#     for i in user_txt:
#         user_text.write(i + " \n")