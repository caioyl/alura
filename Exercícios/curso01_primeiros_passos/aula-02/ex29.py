#Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
  print(f'O primeiro número ({n1}) é maior que o segundo.')
else:
  print(f'O segundo número ({n2}) é maior que o primeiro.')