# Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
n = c = 1
qnt_0_25 = qnt_26_50 = qnt_51_75 = qnt_76_100 = 0
while n >= 0:
  n = int(input(f'Digite a idade do {c}º um paciente: '))
  if n >= 0 and n <= 25:
    qnt_0_25 += 1
  elif n >= 26 and n <= 50:
    qnt_26_50 += 1
  elif n >= 51 and n <= 75:
    qnt_51_75 += 1
  elif n >= 75 and n <= 100:
    qnt_76_100 += 1
  c += 1
print(f'A quantidade de pensionistas que têm entre [0-25] é igual a: {qnt_0_25}.')
print(f'A quantidade de pensionistas que têm entre [26-50] é igual a: {qnt_26_50}.')
print(f'A quantidade de pensionistas que têm entre [51-75] é igual a: {qnt_51_75}.')
print(f'A quantidade de pensionistas que têm entre [76-100] é igual a: {qnt_76_100}.')