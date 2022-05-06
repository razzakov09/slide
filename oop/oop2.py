# data = {
# "markers": [{
# "name": "Rixos The Palm Dubai",
# "location": [25.1212, 55.1535]},
# {
# "name": "Shangri-La Hotel",
# "location": [25.2084, 55.2719]},
# {
# "name": "Grand Hyatt",
# "location": [25.2285, 55.3273]}]
# }

# class Hotel:
#     def __init__(self, data):
#         self.__data = data

#     def get_names(self):
#         for i in self.__data.values():
#             for j in i:
#                 print(j['name'])

#     def collect_data(self):
#         for i in self.__data.values():
#             names = (j['name'] for j in i)
#             locations = (j['location'] for j in i)
#         self.__myDict = {tuple(names) : tuple(locations)}
#         return self.__myDict

#     def set_element(self):
#         for i in self.__data.values():
#             for j in i: j['status_id'] = 1

# v1 = Hotel(data)
# v1.get_names()
# print(v1.collect_data())
# v1.set_element()

# 2 ========================================

# class Factory:
#     def engine(self):
#         return 'Двигатель создан'

#     def bridge(self):
#         return 'Ходовая часть создана'


# class Toyota(Factory):
#     def wheels(self):
#         return 'Колёса готовы'

#     def windows(self):
#         return 'Стёкла готовы'


# v1 = Toyota()
# my_list = [v1.engine(), v1.bridge(), v1.wheels(), v1.windows()]
# print(my_list)
    