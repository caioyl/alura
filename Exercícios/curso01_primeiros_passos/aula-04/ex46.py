# Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. O fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
n = int(input('Digite um número para revelar seu fatorial: '))
fatorial = 1
print(f'{n}! = ',end='')
for c in range (n,0,-1):
  if c != 1:
    print(c,'x ',end='')
  else:
    print(c,end='')
  fatorial *= c
print(f' = {fatorial}')