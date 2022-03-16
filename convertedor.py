import requests
from bs4 import BeautifulSoup

# faz a busca dos dados, e organiza em uma lista, e é reponsavel por mostar o menu de numero + nome do pais
def lista():
  # puxa as informações do site para a variavel
  url = "https://www.iban.com/currency-codes"
  r_iban = requests.get(url)
  # pega apenas o html
  html_iban = r_iban.text
  # organiza o html
  html_organizado = BeautifulSoup(html_iban,"html.parser")
  #pega um card da tag tbody
  tabela = html_organizado.find("tbody")
  linhas = tabela.find_all("tr")

  # joga todos os nomes das moedas da tag td dentro de uma lista
  lista_dict = []
  count = 0
  for linha in linhas:
    count += 1
    itens = linha.find_all("td")
    nome = itens[0].text
    currency_nome = itens[1].text
    moeda = itens[2].text
    
    lista = {
    "count" : count,
    "name_moeda" : nome,
    "currency" : currency_nome,
    "codigo_moeda" : moeda
    } 
    lista_dict.append(lista)
  
  
  return lista_dict
# link conversor
# https://transferwise.com/gb/currency-converter/nio-to-usd-rate?amount=15000

def converte(origem, destino, value):
  # puxa as informações do site para a variavel
    
  url = f"https://transferwise.com/gb/currency-converter/{origem}-to-{destino}-rate?amount={value}"
  
  r_iban = requests.get(url)
  # pega apenas o html
  html_iban = r_iban.text
  # organiza o html
  html_organizado = BeautifulSoup(html_iban,"html.parser")
  #pega um card da tag tbody
    
  valor_moeda = html_organizado.find("span",class_="text-success").string
  
  value_entrada = float(value)

  conversao = (value_entrada * float(valor_moeda))

  return conversao