# Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
#Com função

#Leitura do número
num = int(input('Digite um número inteiro de 1 a 10: '))

#Definição da função:
def tabuada(num: int):
  print(f'Tabuada do {num}')
  for i in range(0,11):
    produto = num * i
    print(f'{num} x {i} = {produto}')
#Chamando a função
tabuada(num)
