# Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:
# "O estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor de [menor] pontos e foi [situacao].

#Declarando a variável notas
notas = []
#Lendo as notas
for i in range(1,5):
  nota = int(input(f'Digite a {i}ª nota: '))
  notas.append(nota)

#Definindo a função que retorna as notas, média e situação

def cadastro (notas: list):
  maior = max(notas)
  menor = min(notas)
  media = sum(notas) / len(notas)
  if media >= 6:
    situacao = "Aprovado(a)"
  else:
    situacao = "Reprovado(a)"
  return media, maior, menor, situacao

media, maior, menor, situacao = cadastro(notas)

print(f'O estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor de {menor} pontos e foi {situacao}.')