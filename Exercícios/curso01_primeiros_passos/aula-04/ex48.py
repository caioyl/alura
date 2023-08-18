# Os números primos possuem várias aplicações dentro da Ciência de Dados, por exemplo, na criptografia e segurança. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
n = int(input('Digite um número para revelar se ele é ou não primo: '))
if n > 1:
  for c in range(2,n):
    if n % c == 0:
      print('Este número não é primo.')
      break
    else:
      print('Este número é primo.')
      break
else:
  print('Este número não é válido.')
