# Escreva um código que lê a lista abaixo e faça:
#
# # lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# A leitura do tamanho da lista
# A leitura do maior e menor valor
# A soma dos valores da lista
#Com função

#Leitura da lista
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#Definindo a função
def leitura(lista):
  #Lendo tamanho, maior e menor número
  tam = len(lista)
  maior = max(lista)
  menor = min(lista)
  soma = 0
  #Soma dos valores pares
  for i in lista:
    if i % 2 == 0:
      soma += i
  #Exibindo o texto
  print(f'A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valors pares presentes nela é igual a {soma}.')
leitura(lista)
