from convertedor import lista

## menu origem
def menu_origem():
  list = lista()
  try:
    entrada = int(input("#: "))
    if entrada > len(list):
      print("\nValor errado, digite apenas um números válido.")
      menu_origem()
    elif entrada == 0:
      print("Programa fechado com sucesso!!")
      return
    else:
      for i in list:
        if i["count"] == entrada:
          if i["currency"] == "No universal currency":
            print(f"\n{i['name_moeda']} não tem uma moeda para o país.")
            menu_origem()
          else:
            if entrada == i["count"]:
              print(f"$$ {entrada}")
              print(f"( x ) {i['name_moeda']}")
              return entrada
  except:
    print("\nIsso não é um número")
    menu_origem()
    
  


## menu destino
def menu_destino():
  list = lista()
  try:
    entrada = int(input("#: "))
    if entrada > len(list):
      print("\nValor errado, digite apenas um números válido.")
      menu_destino()
    elif entrada == 0:
      print("Programa fechado com sucesso!!")
      return
    else:
      for i in list:
        if i["count"] == entrada:
          if i["currency"] == "No universal currency":
            print(f"\n{i['name_moeda']} não tem uma moeda para o país.")
            menu_destino()
          else:
            if entrada == i["count"]:
              return entrada
  except:
    print("\nIsso não é um número")
    menu_destino()

    


# menu valor
def valor():
  try:
    entrada = float(input("#: "))
    if type(entrada) == float:
      return entrada
  except:
    print("Isso não é um número!")
    valor()
    