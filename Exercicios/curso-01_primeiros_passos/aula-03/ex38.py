# Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
pergunta = input('Qual operação você deseja realizar?\nAdição [1]\nSubtração [2]\nMultipliacação [3]\nDivisão [4].\n')
if pergunta in '1234':
  if pergunta == '1':
    resultado = n1 + n2
    print(f'A soma estre estes números é igual a: {resultado}.')
  if pergunta == '2':
    resultado = n1 - n2
    print(f'A subtração entre estes números é igual a: {resultado}.')
  if pergunta == '3':
    resultado = n1 * n2
    print(f'A subtração entre estes números é igual a: {resultado}.')
  if pergunta == '4':
    resultado = n1 / n2
    print(f'A subtração entre estes números é igual a: {resultado}')
else:
  print('Resposta inválida.')
if resultado % 2 == 0:
  parouimpar = 'par'
else:
  parouimpar = 'ímpar'
if resultado > 0:
  positivoounegativo = 'positivo'
else:
  positivoounegativo = 'negativo'
if resultado % 1 == 0:
  inteirooudecimal = 'inteiro'
else:
  inteirooudecimal = 'decimal'
print(f'Este número é {parouimpar},',f'{positivoounegativo}','e',f'{inteirooudecimal}.')