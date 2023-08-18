# Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
# numeros = [2, 8, 15, 23, 91, 112, 256]
# Informe no final quais números possuem raízes inteiras e seus respectivos valores.

from math import sqrt
numeros = [2, 8, 15, 23, 91, 112, 256]
for i in numeros:
    num = sqrt(i)
    print(f'Raiz de {i}: {num} é inteiro? :', num // 1 == num)
