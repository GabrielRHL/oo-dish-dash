import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    json_info = response.json()
    restaurant_info = {}
    for item in json_info:
        restaurant_name = item['Company']
        if restaurant_name not in restaurant_info:
            restaurant_info[restaurant_name] = []

        restaurant_info[restaurant_name].append({"item": item['Item'], "price": item['price'], "description": item['description']})
else:
    print(f'Ocorreu um erro, código do erro: {response.status_code}')

for restaurant_name, info in restaurant_info.items():
    archive_name = f'{restaurant_name}.json'
    with open(archive_name, 'w') as restaurant_archive:
        json.dump(info, restaurant_archive, indent = 4)