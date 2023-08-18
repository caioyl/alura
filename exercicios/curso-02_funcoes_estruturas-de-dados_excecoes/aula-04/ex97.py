# Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
lista = ['2', 2, '33', 50, 30, '5']
def conversor_para_float(lista):
  lista_convertida = [float(lista[i]) for i in range(len(lista))]
  return lista_convertida
conversor_para_float(lista)