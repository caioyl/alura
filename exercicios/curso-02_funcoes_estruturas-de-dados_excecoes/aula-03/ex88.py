# Crie uma lista usando o list comprehension que armazena somente o valor número de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas: aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

lista_tuplas = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento']
print(lista_tuplas)
