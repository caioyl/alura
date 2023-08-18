#Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
  print('Este número é par.')
else:
  print('Este número é ímpar.')