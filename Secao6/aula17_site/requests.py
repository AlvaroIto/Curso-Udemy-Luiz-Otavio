#requests para requisições HTTP
import requests


url = 'http://localhost:8000/'
response = requests.get(url)
print(response.status_code)
print(response.text)