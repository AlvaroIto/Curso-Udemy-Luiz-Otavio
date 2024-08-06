#Usamos a pathlib para trabalhar com caminhos, pastas e arquivos de forma que um código funcione em Windows, Linux e Mac

from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(f'Caminho do projeto: {caminho_projeto.absolute()}')

caminho_arquivo = Path(__file__)
print(f'Caminho do arquivo: {caminho_arquivo}')

#criar um arquivo
arquivo = Path.home() / 'Documentos' / 'arquivo.txt'

arquivo.touch()
print(arquivo)
arquivo.write_text('Olá Mundo')
print(arquivo.read_text())
arquivo.unlink()


#criar uma pasta
caminho_pasta = arquivo = Path.home() / 'Documentos' / 'Python'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)
outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')
#deletar pasta
rmtree(caminho_pasta)


