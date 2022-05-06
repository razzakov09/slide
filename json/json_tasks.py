# 1.С помощью requests получите данные по адресу https://api.github.com/emojis и
# вытащите .json() объект

# import requests
# r = requests.get('https://api.github.com/emojis').json()
# print(r)


# 2.Сделайте POST запрос по адресу https://httpbin.org/post и отправьте туда 
# json ОБЪЕКТ {"name": <Ваше Имя>,"model":<Модель Вашего Ноутбука>}. 

# import requests
# data = requests.post(url='https://httpbin.org/post', json={"name": "Avtandil", "model": "Acer"})
# print(data.json())


# 3.Через psycopg2 подключитесь к удалённой БД, параметры подключения 
# смотрите по адресу <Server IP>/kayrat_db

# ---------------------------------


# 4.Сделайте POST запрос на <Server IP>/upload_to_database. В POST Вам нужно ОБЯЗАТЕЛЬНО
# передать {"name":<Имя Вашего Linux пользователя!>,"date_created":<Настоящее время в
# формате TIMESTAMP>}



