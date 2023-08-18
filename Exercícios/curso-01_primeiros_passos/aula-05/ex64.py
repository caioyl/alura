# Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área da floresta e armazenaram essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
#
# # {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}
# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
dic = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
area_maior = ''
diversidade_maior = 0
for chaves, valores in dic.items():
  media = sum(valores)/len(valores)
  especies = sum(valores)
  print(f'A média da área {chaves} é de {media} espécies.')
  if especies > diversidade_maior:
    diversidade_maior = especies
    area_maior = chaves

print(f'A área com maior diversidade biológica é a {area_maior}, com {diversidade_maior} espécies.')
