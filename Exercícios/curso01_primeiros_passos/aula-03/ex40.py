# Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
combustivel = input('Digite o tipo de combustível:\nDiesel [D]\nEtanol [E]\n')
litros = int(input('Quantos litros de combustível você deseja? '))
if combustivel in 'DE':
  if combustivel == 'D':
    preco = 2
    if litros <= 15:
      desconto = 0.02
    else:
      desconto = 0.04
    print(f'O valor a ser pago será: {preco*litros-(preco*litros*desconto)}')
  else:
    preco = 1.7
    if litros <= 15:
      desconto = 0.03
    else:
      desconto = 0.05
    print(f'O valor a ser pago será: {preco*litros-(combustivel*litros*desconto)}')
else:
  print('Combustível inválido')