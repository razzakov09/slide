print('\nProblem 1')
a = 2**3
b = 3**2
if a > b:
    print(a)
else:
    print(b)

print('\nProblem 2')
a = 3
b = 2
c = 1
if a > b and b > c:
    print('Самое большое число: a \n Самое маленькое число: c')
elif b > a and a > c:
    print('Самое большое число: b \n Самое маленькое число: c')
else:
    print('Самое большое число: c')
    if (a > b):
        print('Самое маленькое число: b')
    else:
        print('Самое маленькое число: a')

print('\nProblem 3')
a = 17391 % 17
b = 546 % 17
c = 934 % 17

if a < b and a < c:
    print('Остаток меньше всего в 17391')
elif b < a and b < c:
    print('Остаток меньше всего в 546')
else:
    print('Остаток меньше всего в 934')

print('\nProblem 4')
x = 13**2
if (x < 172):
    x = x**2
    print(x)

print('\nProblem 5')
n = 123
if n % 2 == 0:
    print('Число четное')
    if n % 3 == 0:
        print('Число делится на 3 без остатка')
        if n**2 > 1000:
            print('Чиcло больше 1000')
        elif n**2 < 1000:
            print('Чиcло меньше 1000')
    else:
        print('Число не делится на 3 без остатка')
        if n**2 > 1000:
            print('Чиcло больше 1000')
        elif n**2 < 1000:
            print('Чиcло меньше 1000')
else:
    print('Число нечетное')
    if n % 3 == 0:
        print('Число делится на 3 без остатка')
        if n**2 > 1000:
            print('Чиcло больше 1000')
        elif n**2 < 1000:
            print('Чиcло меньше 1000')
    else:
        print('Число не делится на 3 без остатка')
        if n**2 > 1000:
            print('Чиcло больше 1000')
        elif n**2 < 1000:
            print('Чиcло меньше 1000')


print('\nProblem 6')
x = 21
if (x > 0 and x < 21):
    print('Число не запрещенное')
else:
    if x > 57 and x < 100:
        print('Число не запрещенное')
    else:
        print('Число запрещенное')

print('\nProblem 7')
x = 5
if x > 2:
    print('Сработал if')
else:
    print('По любому сработает')

print('\nProblem 8')
a = 1
b = 2
c = 3
if a < b:
    if b < c:
        if c > 0:
            print(c)
        else:
            print('c отрицательный')

print('\nProblem 9')
a = 10 // 5
b = 10 / 5
if a == b:
    print(a + b)

print('\nProblem 10')
x = 1
if x < 0:
    print(x)

print('\nProblem 11')
a = 10
b = 5
if a > 0 and b > 0:
    print('Переменные положительны')

print('\nProblem 12')
if a > b:
    print(a+2)
else:
    print(b+2)
        

        
