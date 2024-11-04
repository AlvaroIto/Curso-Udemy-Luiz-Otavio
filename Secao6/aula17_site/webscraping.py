"""
Web Scraping com Python usando requests e bs4 (BeautifulSoup)
Web Scraping é o ato de 'raspar a web' buscando informações de forma automatizadda, com determinada linguagem de programação, para uso posterior. 
O módulo reuqests consegue carregar dados da internet para dentro do seu código. Já o bs4  é responsável por interpretar os dados HTML em formado de objetos Python para facilitar a vida do desenvolvedor

"""
import re
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

#print(parsed_html.title)
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
#print(top_jobs_heading.text)
article = top_jobs_heading.parent
#print(article)
#selecionar todos os paragrafos
for p in article.select('p'):
    print(re.sub(r'\s{1,}', ' ', p.text).strip())


