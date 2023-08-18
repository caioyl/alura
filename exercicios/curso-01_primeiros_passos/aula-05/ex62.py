# Uma pesquisa de mercado foi feita para decidir qual design de uma marca infantil mais agrada crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
#
# # Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos
# Adapte os dados fornecidos a você para uma estrutura de dicionário e a partir dele, informe o design vencedor e a porcentagem de votos recebidos.
tabela_votos = {'Design_1':1334,'Design_2':982,'Design_3':1751,'Design_4':210,'Design_5':1811}
votos_totais = 0
vencedor = ''
mais_votos = 0
for design, votos in tabela_votos.items():
  votos_totais += votos
  if votos > mais_votos:
    mais_votos = votos
    vencedor = design
porcentagem = mais_votos/votos_totais * 100
print(f'O design vencedor foi o {vencedor}, com {porcentagem:.2f}% dos votos.')