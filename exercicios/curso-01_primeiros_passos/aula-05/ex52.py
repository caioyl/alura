# Com os mesmos dados da questão anterior, defina quantas compras foram acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
qnt_gastos = 0
for gastos in lista:
  if gastos > 3000:
    qnt_gastos += 1
print(f'A quantidade de gastos acima de R$3000,00 é igual a: {qnt_gastos}.\nA porcentagem que isso representa em relação ao total de compras é: {qnt_gastos/len(lista)*100:.1f}%.')