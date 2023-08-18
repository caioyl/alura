# Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e faça uma análise. Portanto, escreva um programa que leia temperaturas e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
temperatura = quantidade = temperaturas = 0
while temperatura != -273:
  temperatura = float(input('Digite a temperatura em Celsius: '))
  if temperatura != -273:
    temperaturas += temperatura
    quantidade += 1
print(f'A média é igual a: {temperaturas/quantidade}ºC.')
