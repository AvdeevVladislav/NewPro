import requests

def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat

apikey = '73e1cb3d-c310-4810-b6ba-4e7be9a6f0d1'  # ключ

coords = fetch_coordinates(apikey, "метро Маяковская")
print(coords)

coords = fetch_coordinates(apikey, "метро Каширская")
print(coords)

coords = fetch_coordinates(apikey, "улица Туровская")
print(coords)
