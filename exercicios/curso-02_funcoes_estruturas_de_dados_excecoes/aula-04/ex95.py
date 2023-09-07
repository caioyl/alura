# Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0 e também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.
try:
  n1 = float(input('Digite o primeiro número: '))
  n2 = float(input('Digite o segundo número: '))
  divisao = n1/n2
except Exception as e:
  print(type(e),f'Erro: ',e)
