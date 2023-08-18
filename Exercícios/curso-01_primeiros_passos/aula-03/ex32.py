#Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
preco1 = int(input('Digite o valor do preço de um carro no primeiro ano: '))
preco2 = int(input('Digite o valor do preço de um carro no segundo ano: '))
preco3 = int(input('Digite o valor do preço de um carro no terceiro ano: '))
maior = preco1
menor = preco1
if preco2 > maior:
  maior = preco2
else:
  menor = preco2
if preco3 > maior:
  maior = preco3
else:
  menor = preco3
print(maior)
print(menor)