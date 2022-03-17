# 1
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
drinks = ['Coca-Cola', 'Sprite', 'Fanta']
menu['drinks'] = drinks

# 2
my_dict2 = {}
for i in range(3):
    name = input('Input your name: ')
    password = input('')
    my_dict2[name] = password

# 3
my_dict3 = {}
names_and_professions = [
    ['Avtandil', 'Сантехник'],
    ['Sanjar', 'Сварщик'],
    ['Kairat', 'Электрик'],
    ['Azat', 'Инженер'],
    ['Oleg', 'Менеджер']]

for i in names_and_professions:
    my_dict3[i[0]] = i[1]
print(my_dict3)

# 4
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu['Besh_barmak'] = 130
print(menu)
menu['Besh_barmak'] = 135
print(menu)
menu.pop('borsh')
print(menu)

# 5
south_american_countries = [
    'Argentina', 'Bolivia', 'Brazil',
    'Chile', 'Colombia', 'Ecuador',
    'Guyana', 'Paraguay', 'Peru',
    'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

new_dictionary = {}

cnt = 1
for i in set(south_american_countries):
    new_dictionary[cnt] = i
    cnt += 1
print(new_dictionary)




        