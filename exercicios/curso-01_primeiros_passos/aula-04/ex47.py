# Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
n = int(input('Digite um número para revelar sua tabuada: '))
if n > 0 and n <= 10:
  for c in range(1,11):
    print(f'{n} x {c} = {n*c}')
else:
  print('Número inválido.')