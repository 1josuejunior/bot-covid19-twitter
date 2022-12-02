# Fases do projeto do Bot da Covid-19 no Brasil e Mundo.

# 1 - Capturar os dados de um site em tempo real.
# 2 - Organizar esses dados.
# 3 - Integrar com o Twitter.

import requests
from bs4 import BeautifulSoup

# Informações do Brasil

page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.findAll("div", {"class": "maincounter-number"})

cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

brasil = ("🇧🇷 Total de casos confirmados no Brasil: \n"+ \
    "Casos confirmados: " + container[0].text.strip() + "\n" + \
    "Óbitos: " + container[1].text.strip() + "\n" + \
    "Recuperações: " + container[2].text.strip() + "\n\n")

# Informações do Mundo 

page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.findAll("div", {"class": "maincounter-number"})

cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip()

mundo = ("Total de casos confirmados no Mundo: \n"+ \
    "Casos confirmados: " + container[0].text.strip() + "\n" + \
    "Óbitos: " + container[1].text.strip() + "\n" + \
    "Recuperações: " + container[2].text.strip() + "\n\n")

print(brasil)
print(mundo)