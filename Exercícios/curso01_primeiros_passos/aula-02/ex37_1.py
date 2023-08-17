#Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
n = float(input('Digite um número: '))
if n - int(n) == 0:
  print('Este número é inteiro.')
else:
  print('Este número é decimal')