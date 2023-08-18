# Faça um programa que, ao inserir um número qualquer, criará uma lista contendo todos os números primos entre 1 e o número digitado.
numero = int(input('Digite um número para revelar todos os números primos entre 1 e ele: '))
lista_primos = [1]
for i in range(2,numero+1):
  primo = True
  for c in range(2,i):
    if i % c == 0:
      primo = False
      break
  if primo:
    lista_primos.append(i)
print(lista_primos)

#Opção 1:Criar uma lista e adicionar os valores que são divisíveis pelo número. Se a lista estiver vazia, adicionar ele à lista dos primos. Zerar a lista.
#Opção 2: Usar booleano