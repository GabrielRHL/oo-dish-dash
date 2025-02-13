import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    json_info = response.json()
    print(json_info)
else:
    print(f'Ocorreu um erro, código do erro: {response.status_code}')