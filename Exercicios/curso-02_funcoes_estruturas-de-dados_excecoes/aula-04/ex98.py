# Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'
# Dados para testar a função:
# Valores sem erro:
# lista1 = [4,6,7,9,10]
# lista2 = [-4,6,8,7,9]
# Listas com tamanhos diferentes:
# lista1 = [4,6,7,9,10,4]
# lista2 = [-4,6,8,7,9]
# Listas com valores incoerentes:
# lista1 = [4,6,7,9,'A']
# lista2 = [-4,'E',8,7,9]

lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]
lista3 = [4,6,7,9,10,4]
lista4 = [-4,6,8,7,9]
lista5 = [4,6,7,9,'A']
lista6 = [-4,'E',8,7,9]

def funcao(l1,l2):
  try:
    lista_nova = [(l1[i],l2[i],l1[i]+l2[i]) for i in range(len(l1))]
  except IndexError:
    print('A quantidade de elementos em cada lista é diferente.')
  except TypeError:
    print('Pelo menos uma das listas têm valores não númericos.')
  else:
    return lista_nova
funcao(lista5,lista2)
