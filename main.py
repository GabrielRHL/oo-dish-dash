from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    '''
    Endpoint que exibe os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_info = response.json()
        if restaurant is None:
            return {'Dados': json_info}
        restaurant_info = []
        for item in json_info:
            if item['Company'] == restaurant:
                restaurant_info.append({"item": item['Item'], "price": item['price'], "description": item['description']})
        return {'Restaurante': restaurant, 'Cardapio': restaurant_info}
    else:
        return {'Erro': f'{response.status_code}'}