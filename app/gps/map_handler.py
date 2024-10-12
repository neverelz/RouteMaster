import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Проверка переменных окружения
if API_KEY is None:
    print("API_KEY is not set.")
if BASE_URL is None:
    print("BASE_URL is not set.")

# Проверка наличия API-ключа
if API_KEY is None:
    print("API_KEY is not set.")
else:
    # Пример запроса для получения координат по адресу
    params = {
        'geocode': 'Москва, Красная площадь',  # Адрес для геокодирования
        'apikey': API_KEY,                      # Ваш API-ключ
        'format': 'json'                        # Формат ответа (JSON)
    }

# Выполняем GET-запрос к API
response = requests.get(BASE_URL, params=params)
data = response.json()


# Проверка наличия ошибок
if 'error' in data:
    print("Ошибка от API:", data['error'])
else:
    if data.get('response', {}).get('GeoObjectCollection', {}).get('featureMember'):
        location = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = location.split()  # Разделяем долготу и широту
    else:
        print("Нет данных для указанного адреса.")