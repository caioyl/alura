# Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do seu salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada funcionário não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos funcionários receberam o abono mínimo e qual o maior valor de abono fornecido.
salarios_abono = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
salarios_atuais = {}
gasto_abonos = maior = qnt_abono_minimo = 0
for posicoes in range(0,len(salarios_abono)):
  if salarios_abono[posicoes] * 0.1 > 200:
    salario_atual = salarios_abono[posicoes] * 1.1
    abono = salario_atual - salarios_abono[posicoes]
    salarios_atuais[salarios_abono[posicoes]] = abono
  else:
    salario_atual = salarios_abono[posicoes] + 200
    abono = salario_atual - salarios_abono[posicoes]
    salarios_atuais[salarios_abono[posicoes]] = abono
    qnt_abono_minimo += 1
  gasto_abonos += abono

for valores in salarios_atuais.values():
  if valores > maior:
    maior = valores

print(f'Abonos: {salarios_atuais}\nO gasto total com os abonos foi R${gasto_abonos:.2f}.\n{qnt_abono_minimo} funcionários receberam o abono mínimo de R$200,00.\nO maior abono recebido foi de: R${maior:.2f}')