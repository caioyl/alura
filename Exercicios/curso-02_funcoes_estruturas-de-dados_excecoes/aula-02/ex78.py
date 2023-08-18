# Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

# Leitura da lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda para calcular o quadrado de cada elemento da lista
quadrados = list(map(lambda x: x**2,lista))
# Chamando a lista
print(quadrados)