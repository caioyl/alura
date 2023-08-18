# Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

#Declarando a lista
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

#Imprimindo cada um dos elementos com uma divisão entre eles

#Iterando cada lista da lista de listas
for i in range(len(lista_de_listas)):
  print('A soma entre: \n')
  #Iterando cada item de cada lista da lista de listas
  for c in range(len(lista_de_listas[i])):
    print(lista_de_listas[i][c])
  #Imprimindo a soma dos elementos de cada lista
  print(f'\nÉ igual a: {sum(lista_de_listas[i])}\n')