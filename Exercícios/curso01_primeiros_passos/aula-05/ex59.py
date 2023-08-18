# Desenvolva um programa que informa a nota de um aluno de acordo com suas respostas. Ele deve pedir a resposta de um aluno para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem alternativas: A, B, C ou D.
# Gabarito da Prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B
notas = []
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
pontuacao = 0
for c in range(1,11):
  nota = input(f'Digite a resposta da questão {c}: ')
  notas.append(nota)

for c in range(1,11):
  if notas[c-1] == gabarito[c-1]:
    print(f'\033[92m{notas[c-1]}')
    pontuacao += 1
  else:
    print(f'\033[91m{notas[c-1]} ',end='')
    print(f'\033[0;0mResposta correta: \033[92m{gabarito[c-1]}')

print(f'\033[0;0A nota do aluno foi igual a: {pontuacao}')
