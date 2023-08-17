# Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno.
l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite outro lado do triângulo: '))
l3 = int(input('Digite mais um lado do triângulo: '))
if l1 + l2 > l3 or l1 + l3 > l3 or l2 + l3 > l1 or l3 + l1 > l2:
  if l1 == l2 == l3:
    print('Este triângulo é equilátero.')
  elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Este triângulo é isósceles.')
  else:
    print('Este triângulo é escaleno.')
else:
  print('Estes lados não formam um triângulo.')