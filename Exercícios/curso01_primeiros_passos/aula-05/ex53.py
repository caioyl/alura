# Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
lista_3 = []
for contador in range(1,6):
  elemento = int(input(f'Digite o {contador}º número a ser adicionado à lista: '))
  lista_3.append(elemento)
lista_3