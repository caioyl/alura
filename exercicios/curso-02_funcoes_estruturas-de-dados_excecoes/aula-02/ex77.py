# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
# Utilize o return na função e salve a nova lista na variável mult_3.

# Leitura da lista
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Definindo a lista com múltiplos de 3
mult_3 = []

# Definição da função que insere números na lista de múltiplos de 3:
def multiplo_3(lista: list) -> list:
  for i in lista:
    # Condição para incluir número na lista dos múltiplos de 3
    if i % 3 == 0:
      # Adicionando os números à lista
      mult_3.append(i)
  return mult_3

# Inserindo o resultado da função (mult_3 local) na mult_3 global
mult_3 = multiplo_3(lista)
print(mult_3)