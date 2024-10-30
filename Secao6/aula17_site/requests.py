#requests para requisições HTTP
import requests


url = 'http://localhost:8000/'
try:
    response = requests.get(url)
    response.raise_for_status()  # Lança um erro se o status não for 200
    print(f'Resposta: {response.text}')
except requests.exceptions.RequestException as e:
    print(f'Erro na requisição: {e}')

input("Pressione Enter para sair...")