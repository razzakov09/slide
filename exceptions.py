# 1 Напишите код где есть TypeError,IndexError,NameError

# try:
#     a = int(input("Введите число: "))
#     b = input("Введите текст ")
#     print(b[1])
#     print(z)
# except TypeError:
#     print(TypeError)
# except IndexError:
#     print(IndexError)
# except NameError:
#     print(NameError)

# 2 Возьмите код #1 и создайте для него try... except... 
# Создайте несколько except выражений для разных типов ошибок

# try:
#     at = 10
#     iin = 15
#     wo = 20
#     for e in range(-at, at):
#         print(wo / e)
#         if at > '5':
#             print("at > 5")
# except TypeError:
#     print(TypeError)

# Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.

# try:
#     lst = []

#     for i in range(10):
#         lst.append(i)

#     a = list(reversed(lst))
#     sls_obj = (a[0:8])
#     print(sls_obj)
# except NameError:
#     print(NameError)
# except AttributeError:
#     print(AttributeError)
# except TypeError:
#     print(TypeError)

# Перенесите к себе код #3 и исправьте все ошибки, сделайте так чтобы код работал. 
# Если не знаете как исправить ошибку создайте для неё except выражение.

# try:
#     a = (0)
#     b = (1)
#     numbers = 0

#     while b < a:
#         numbers += b
#         b += 1
# except IndentationError:
#     print(IndentationError)
# except TypeError:
#     print(TypeError)