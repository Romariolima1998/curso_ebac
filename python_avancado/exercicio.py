import requests
from bs4 import BeautifulSoup

# URL da página com a lista dos filmes
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

# Faz a requisição da página
response = requests.get(url,headers=headers)

# Extrai o conteúdo da página
html = response.content

# Cria um objeto BeautifulSoup para parsear o conteúdo da página
soup = BeautifulSoup(html, "html.parser")

# Encontra a tag <ul> com a classe "ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base"
ul = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-9d2f6de0-0 iMNUXk compact-list-view ipc-metadata-list--base")


# Coleta o título e a classificação de cada filme
filmes = []
for li in ul.find_all("li"):
    
    # Encontra o elemento <a> com a classe "title"
    a = li.find("h3", class_="ipc-title__text")
    title = a.text
    print(title)

    # Encontra o elemento <div> com a classe "rating"
    div = li.find("div", class_="sc-94da5b1b-0 soBIM meter-const-ranking sc-479faa3c-6 glWBvR cli-meter-title-header")
    rating = div.text

    # Cria um dicionário com as informações do filme
    filme = {"titulo": title, "classificacao": rating}

    # Adiciona o dicionário à lista de filmes
    filmes.append(filme)

    # Abre o arquivo CSV para escrita

# Imprime a lista de filmes
for filme in filmes:
    print(filme)