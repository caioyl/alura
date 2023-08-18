# Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
#Para variação acima de 20%: bonificação para o time de vendas.
#Para variação entre 2% e 20%: pequena bonificação para time de vendas.
#Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
#Para bonificações abaixo de -10%: corte de gastos.
qnt_de_vendas2022 = int(input('Digite quantas vendas foram feitas em 2022: '))
qnt_de_vendas2023 = int(input('Digite quantas vendas foram feitas em 2023: '))
if qnt_de_vendas2023/qnt_de_vendas2022 > 1.20:
  print('Bonificação para o time de vendas.')
elif qnt_de_vendas2023/qnt_de_vendas2022 > 1.02 and qnt_de_vendas2023/qnt_de_vendas2022 <= 1.2:
  print('Pequena bonificação para o time de vendas.')
elif qnt_de_vendas2023/qnt_de_vendas2022 < 1.2 and qnt_de_vendas2023/qnt_de_vendas2022 > 0.9:
  print('Incentivo às vendas.')
elif qnt_de_vendas2023/qnt_de_vendas2022 < 0.9:
  print('Corte de gastos.')