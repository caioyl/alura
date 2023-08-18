#Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
letra = input('Digite uma letra: ')
if letra in 'aeiou':
  print('Esta letra é uma vogal.')
else:
  print('Esta letra é uma consoante.')