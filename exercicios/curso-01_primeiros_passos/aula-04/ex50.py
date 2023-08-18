# Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva um programa que calcule o vencedor da eleição. A votação ocorreu da seguinte maneira:
# Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4). Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6). Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
n = votos_1 = votos_2 = votos_3 = votos_4 = votos_nulos = votos_brancos = quantidade_de_votos = vencedor = 0
for c in range (1,21):
  print(f'{c}º Voto:\n')
  n = int(input(f'VOTE EM UM DOS CANDIDATOS:\nCANDIDATO [1]\nCANDIDATO [2]\nCANDIDATO [3]\nCANDIDATO [4]\nVOTO NULO [5]\nVOTO BRANCO [6]\n'))
  if n == 1:
    votos_1 += 1
  elif n == 2:
    votos_2 += 1
  elif n == 3:
    votos_3 += 1
  elif n == 4:
    votos_4 += 1
  elif n == 5:
    votos_nulos += 1
  elif n == 6:
    votos_brancos += 1
  else:
    print('Voto inválido.')
print(f'Votos candidato 1: {votos_1}')
print(f'Votos candidato 2: {votos_2}')
print(f'Votos candidato 3: {votos_3}')
print(f'Votos candidato 4: {votos_4}')
print(f'A porcentagem de votos nulos foi igual a: {votos_nulos/20}')
print(f'A porcentagem de votos nulos foi igual a: {votos_brancos/20}')