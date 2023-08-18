# Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome
#
# As listas são:
# nomes = ["joão","MaRia", "JOSÉ"]
# sobrenomes  ["SILVA", "souza", "Tavares"
# O texto exibido ao fim deve ser parecido com: "Nome completo: Ana Silva"

#Declarando as variáveis
nomes = ["joão","MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

#Definindo função lambda
nome_completo = list(map(lambda x, y: f'{x.title()} {y.title()}', nomes, sobrenomes))
#OBS: em f'{x.title()} {y.title()}', estamos retornando o resultado da operação de strings como uma string única que contém as duas variáveis transformadas. O f' é usado para chamar as variáveis através das chaves
for i in nome_completo:
  print(f'Nome completo: {i}')
