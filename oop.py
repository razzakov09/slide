class Laptop:
    my_dict = {}

    def __init__(self, model):
        self.my_dict['Модель ноутбука'] = model
    
    def set_property(self):
        print('\nВведите характеристики ноутбука')
        self.my_dict['Процессор'] = input('Процессор: ')
        self.my_dict['Видеокарта'] = input('Видеокарта: ')
        self.my_dict['Оперативка'] = input('Оперативка: ')
        self.my_dict['Жесткий диск'] = input('Жесткий диск: ')
        self.my_dict['Материнская плата'] = input('Материнская плата: ')
        self.my_dict['Размер дисплея'] = input('Размер дисплея: ')

    def get_info(self):
        print('\nХарактеристики вашего ноутбука')
        for k, v in self.my_dict.items():
            print(f'{k} : {v}')

v1 = Laptop('Acer')
v1.set_property()

v2 = Laptop('Asus')
v2.set_property()

v1.get_info()
v2.get_info()