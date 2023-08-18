# Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista = []
for c in range(1,6):
  numeros = int(input('Digite um número: '))
  lista.append(numeros)
for c in range(4,-1,-1):
  print(lista[c],end=' ')