# 1
lang1 = 'php'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if lang1 == i:
        print('this languages is in list')

# 2
for i in languages:
    if i == lang1:
        break
    print(i)

# 3
num = 7
i = 0
while i != 5:
    num *= 7
    i += 1
    print(num)

# 4
for i in range(len(languages)):
    print(str(i), languages[i])

# 5
cnt = 1
cnt2 = 10
while True:
    if cnt < 10:
        print(cnt)
        cnt += 1
    elif cnt >= 10:
        print(cnt2)
        cnt2 -= 1
        if cnt2 == 0:
            break
        
# 6
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
for i in range(len(names)):
    if i % 2 == 0:
        print(names[i])

#7
print()
for i in range(0, len(names), 2):
    print(names[i])

# 8 
x = 231
if len(str(x)) == 3:
    print("Это число трёхзначное!")

if x > 0 and x % 2 == 0:
    print("Это число положительное и чётное!")

if x % 31 == 0:
    print("Это число делится на 31 без остатка!")

if x > 100 and x % 17 == 0 or x > 150 and x == 13**2:
    print(x)

# 9
print()
cnt1 = 0
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        i = i**2
        cnt1 += 1

cnt2 = 0
for i in range(-100, 100, 7):
    if i % 2 != 0:
        cnt2 += 1
        print(i)

print("Под первое условие подходят", cnt1, "чисел")
print("Под второе условие подходят", cnt2, "чисел")