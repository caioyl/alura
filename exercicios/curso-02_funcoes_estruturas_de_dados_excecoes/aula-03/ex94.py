# Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de funcionários e o gestor gostaria de ter um agrupamento da soma de funcionários para cada estado. As informações contidas na tabela são:
# funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
# A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de funcionários referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de funcionários por Estado.
# Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui apenas os valores numéricos de funcionários(as) de cada Estado.
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
#Estados sem repetição
estados_unidades = list(set(funcionario[0] for funcionario in funcionarios))

#Dicionário feito de uma vez só {'SP': 43, 'RJ': 20....,'XX':00}
funcionarios_estado = {estados_unidades[i]:sum([funcionarios[c][1] for c in range(len(funcionarios)) if funcionarios[c][0] == estados_unidades[i]]) for i in range(len(estados_unidades))}

#Listas com quantidades de funcionários por estado
qtd_funcionarios = [sum(funcionarios[c][1] for c in range(len(funcionarios)) if funcionarios[c][0] == estados_unidades[i]) for i in range(len(estados_unidades))]

#Dicionário com as duas informações
funcionarios_estado_melhor_documentado = {estados_unidades[i]:qtd_funcionarios[i] for i in range(len(qtd_funcionarios))}
print(funcionarios_estado_melhor_documentado)