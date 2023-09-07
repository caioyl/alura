# A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

#Sem zip()
lista_de_tuplas = []
#Definindo a lista
lista = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

#Laço for para acessar cada lista
for i in range(len(lista)):
  #Adicionando tupla com posição de cada i
  lista_de_tuplas.append((i,lista[i]))
lista_de_tuplas
