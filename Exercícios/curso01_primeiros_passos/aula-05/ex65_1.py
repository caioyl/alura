# O setor de RH da sua empresa te pediu uma ajuda para analisar as idades dos funcionários de 4 setores da empresa. Para isso, ele te forneceu os seguintes dados:
#
# # {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Sabendo que cada setor tem 10 funcionários, construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
qnt_acima_media = somatoria = qnt_funcionarios = 0

for setor, ids in idades.items():
  media = sum(ids)/len(ids)
  print(f'A média do {setor} é igual a {media}.')
  somatoria += sum(ids)
  qnt_funcionarios += len(ids)
  media_total = somatoria/qnt_funcionarios

for setor, idades in idades.items():
  for id in idades:
    if id > media_total:
      qnt_acima_media += 1
print(f'A média total é {media_total}. {qnt_acima_media} deles estão acima da idade média geral.')
