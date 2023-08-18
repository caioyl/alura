# Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas: lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
#Com list comprehension

#Definindo a lista
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
#Criando a lista com os terceiros elementos de cada tupla
lista_terceiros = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
print(lista_terceiros)