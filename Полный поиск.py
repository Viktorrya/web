import requests
from choose_spn import spn

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = '9bd25a98-6d1c-4e0f-82f4-6067d7c1058f'

address_ll = "37.588392,55.734036"

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass
# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первую найденную организацию.
organization = json_response["features"][0]
print(organization)
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]
org_size = spn(organization)

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])
delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": "{0},pm2dgl".format(org_point)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)