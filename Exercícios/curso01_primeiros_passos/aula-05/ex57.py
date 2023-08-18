# Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
# Lista de crescimento das bactérias
lista_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# Lista que irá armazenar as porcentagens de crescimento
lista_crescimento = []
# Vamos percorrer os índices de 1 a 9 para compararmos o valor atual com o passado
for c in range (1,len(lista_bacterias)):
  # seguimos o cálculo 100 * (amostra_atual - amostra_passada) / (amostra_passada)
  taxa_crescimento = 100 * (lista_bacterias[c] - lista_bacterias[c-1])/lista_bacterias[c-1]
  # adicionamos o resultado na lista porcentagem_crescimento
  lista_crescimento.append(taxa_crescimento)
  #Imprimimos a taxa de crescimento de cada dia
  print(f'A taxa de crescimento do dia {c} foi igual a: {taxa_crescimento:.2f}%')
# Resultado
print(f'As porcentagens de crescimento foram iguais a:\n{lista_crescimento}')