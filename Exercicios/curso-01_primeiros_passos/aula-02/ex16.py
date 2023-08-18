#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
n1 = int(input('Digite um numerador: '))
n2 = int(input('Digite um denominador: '))
if n2 == 0:
  print('O denominador não pode ser zero.')
else:
  resto_da_divisao = n1 % n2
  print(resto_da_divisao)