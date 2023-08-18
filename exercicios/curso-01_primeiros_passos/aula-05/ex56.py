# Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é uma data válida para uma análise.
#Verificando se o mês está em uma lista para e aplicar a condição para todos
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2:
  if (ano % 4 == 0) and (ano % 400 == 0 or ano % 100 != 0):
    if dia > 29 or dia < 0:
      print('Data inválida.')
    else:
      print('Data válida.')

elif mes in [2, 4, 6, 8, 10, 12]:
  if dia > 30 or dia < 0:
    print('Data inválida.')
  else:
    print('Data válida.')

elif mes in [1, 3, 5, 7, 9, 11]:
  if dia > 30 or dia < 0:
    print('Data inválida.')
  else:
    print('Data válida.')
elif mes > 12:
  print('Data inválida')