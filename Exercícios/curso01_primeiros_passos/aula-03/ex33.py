#Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
preco1 = int(input('Digite o preço do produto 1: '))
preco2 = int(input('Digite o preço do produto 2: '))
preco3 = int(input('Digite o preço do produto 3: '))
if preco1 < preco2 and preco1 < preco3:
  print('O primeiro produto é mais barato.')
if preco2 < preco1 and preco2 < preco3:
  print('O segundo produto é mais barato.')
else:
  print('O terceiro produto é mais barato.')