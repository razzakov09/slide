# 0
from cgitb import reset


dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)

# 1
a = frozenset({1, 2, 3})
b = frozenset({4, 5, 6})
c = frozenset({9, 8, 7})
result = set([a, b, c])
print(result)

# 2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.difference(farm_1))

# 3
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
my_set.pop()
print(my_set)

# 4
my_new_list = []
for i in range(10):
    x = int(input('Введите значение: '))
    my_new_list.append(x)

my_frozen_set = frozenset(my_new_list)
print(my_frozen_set)

# 5
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
res_farm = farm_1.intersection(farm_2)
print(res_farm)
# part 2
print(farm_1.difference(farm_2))

