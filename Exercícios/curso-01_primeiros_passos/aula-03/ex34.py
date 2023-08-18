#Escreva um programa que leia três números e os exiba em ordem decrescente.
n1 = int(input('Digite o valor do preço de um carro no primeiro ano: '))
n2 = int(input('Digite o valor do preço de um carro no segundo ano: '))
n3 = int(input('Digite o valor do preço de um carro no terceiro ano: '))
if n1 >= n2 and n1 >= n3:
  print(n1)
  if n2 >= n3:
    print(n2)
    print(n3)
  else:
    print(n3)
    print(n2)
elif n2 >= n1 and n2 >= n3:
  print(n2)
  if n1 >= n3:
    print(n1)
    print(n3)
  else:
    print(n3)
    print(n1)
else:
  print(n3)
  if n1 >= n2:
    print(n1)
    print(n2)
  else:
    print(n2)
    print(n1)