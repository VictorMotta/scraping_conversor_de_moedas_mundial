from convertedor import *
from menu import *
import babel.numbers
import decimal

# verifica se o usuario quer fazer uma nova pesquisa, e trata o erro de digitos.
def reiniciar():
  voltar = str(input("\nDeseja verificar novamente? S/N: ")).lower()
  if voltar == "s":
    main()
    return
  if voltar == "n":
    print("Programa fechado com sucesso!!")
    return
  else:
    try:
      print("Erro, Digitou algo errado, digite S para sim e N para não.")
      reiniciar()
    except:
      reiniciar()
      
# puxa os dados para printar tudo que é necessário na tela
def main():
  print("Bem vindo ao Negociador de Moedas!")
  print("Escolha pelo número os dois países que deseja negociar moedas:\n")
  for i in lista(): 
    print(f"# {i['count']} = {i['name_moeda']}")
        
  print("\nCaso queira sair do programa, digite um 0.")
  print("Informe pelo número o pais de origem da moeda\n")

  result_origem = menu_origem()
  print("\nQuer negociar com qual outro país?\n")
  result_destino = menu_destino()
    
  
  for i in lista():
    if result_origem == i["count"]:
      cod_origem = i["codigo_moeda"]

  
  for i in lista():
    if result_destino == i["count"]:
      cod_destino = i["codigo_moeda"]
     
  

  print(f"\nQuantos {cod_origem} você quer converter em {cod_destino}\n")

  result_valor = valor()
  
  result_conversao = converte(cod_origem, cod_destino, result_valor)
  
  valor_formatado = babel.numbers.format_currency( decimal.Decimal( result_valor ), cod_origem )

  valor_formatado_total = babel.numbers.format_currency( decimal.Decimal( result_conversao ), cod_destino )

  print(f"\n{valor_formatado} é igual a {valor_formatado_total}\n")

  reiniciar()


  


main()