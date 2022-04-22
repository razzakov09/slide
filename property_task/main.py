my_dict = {}
with open('text.txt', 'r') as f:
    data = f.readlines()
    for i in data:
        key, value = i.split('=')[0].strip(), i.split('=')[1].strip()
        if key.endswith('\n'): 
            my_dict[key] = value[:-1]
        else:
            my_dict[key] = value


class Hack:
    def __init__(self, host, ip, port, password):
        self.__host = host
        self.__ip = ip
        self.__port = port
        self.__password = password

        self.check_host(host)
        self.check_ip(ip)
        self.check_port(port)
        self.check_password(password)

        print("Success!")

    @classmethod
    def is_digit(cls, value, type_op):
          for i in value:
            if not i.isdigit():
                raise TypeError(f'В {type_op} должны быть числа')

    @classmethod
    def aktet_len(cls, value, type_op):
          if len(value) != 4:
            raise TypeError(f'В {type_op} должны быть 4 актета')

    @classmethod
    def range_aktet(cls, value, type_op):
        for i in value:
            if int(i) < 0 or int(i) > 255:
                raise TypeError(f'{type_op} больше 255 или меньше 0')

    @classmethod
    def check_host(cls, host):
        user_host = host.split('.')

        cls.aktet_len(user_host, 'хосте')
        cls.is_digit(user_host, 'хостe')
        cls.range_aktet(user_host, 'Хост')
        

    @classmethod
    def check_ip(cls, ip):
        user_ip = ip.split('.')

        cls.aktet_len(user_ip, 'ip')
        cls.is_digit(user_ip, 'ip')
        cls.range_aktet(user_ip, 'ip')

    @classmethod
    def check_port(cls, port):
        if type(port) is str:
            if not port.isdigit():
                raise TypeError('В порте должны быть числа')

            port = int(port)

        if port < 1024 or port > 9999:
            raise TypeError('Порт вне диапазона')

    @classmethod
    def check_password(cls, password):
        if type(password) is int:
            print('Пароль должен быть строкой')
        else: 
            if len(password) < 8:
                raise TypeError('Пароль должен быть больше 8 символов')

    @property
    def host(self):
        return self.host

    @host.setter
    def host(self, host):
        self.__host = host

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__host = port

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


v = Hack(**my_dict)
