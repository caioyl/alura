# Escreva um código que lê a lista abaixo e faça:
#
# # lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# A leitura do tamanho da lista
# A leitura do maior e menor valor
# A soma dos valores da lista
#Sem função

#Leitura da lista
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

#Tamanho
tam = len(lista)
#Maior valor
maior = max(lista)
#Menor valor
menor = min(lista)
#Soma dos valores pares
soma = 0
for i in lista:
  if i % 2 == 0:
    soma += i

print(f'A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valors pares presentes nela é igual a {soma}.')