lista = []
for c in range(1,6):
  numeros = int(input('Digite um número: '))
  lista.append(numeros)
print(f'Lista de números invertida: {lista[::-1]}')