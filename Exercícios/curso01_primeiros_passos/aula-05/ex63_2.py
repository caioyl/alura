# Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do seu salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada funcionário não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos funcionários receberam o abono mínimo e qual o maior valor de abono fornecido.
# Lista de salários
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
# Inicializamos as variáveis
dic_abonos = {} # Dicionário de abonos
total_abono = 0 # Irá somar todos os gastos com abono
abonos_minimo = 0 # Irá armazenar a quantidade de abonos mínimos
maior_abono = 0 # Irá armazenar o maior valor de abono

# Percorremos toda a lista de salários
for salario in salarios:
  # Calculamos o valor teórico de abono
  abono = salario * 0.1
  # Caso o abono seja inferior a 200,
  # ajustamos o valor de abono para o mínimo (200)
  if abono < 200:
    abono = 200
  # Adicionamos um novo dado no dicionário chave abono
  dic_abonos[salario] = abono

# Percorremos todos os valores do dicionário de abonos
for abono in dic_abonos.values():
  # Contamos o salário minimo
  if abono == 200:
    abonos_minimo += 1
  # Verificamos se o abono lido é maior que o valor armazenado em maior_abono
  # Cada vez que o abono superar o valor de maior_abono,
  # a variável maior_abono vai ser igual à abono, atribuindo um novo valor
  if abono > maior_abono:
    maior_abono = abono
  # Somamos os abonos
  total_abono += abono
# Resultados
print(f'Abonos: {dic_abonos}')
print(f'Total de gasto com abonos: {total_abono}')
print(f'Número de funcionários que receberam o abono mínimo: {abonos_minimo}')
print(f'Maior valor de abono: {maior_abono}')