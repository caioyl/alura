#Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
percentual_de_crescimento = float(input('Digite o percentual de crescimento de produção da empresa: '))
if percentual_de_crescimento > 0:
  print('Houve crescimento.')
elif percentual_de_crescimento < 0:
  print('Houve decrescimento.')
else:
  print('Não houve crescimento.')