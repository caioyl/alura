# Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
# {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
# 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
# Escreva um código que calcule o total de vendas e o produto mais vendido.
produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
produto_mais_vendido = 0
for produto, vendas in produtos.items():
  if vendas > produto_mais_vendido:
    vendas_mais_vendido = vendas
    nome_do_produto = produto
print(f'O produto mais vendido é o {nome_do_produto}, com {vendas_mais_vendido} vendas.')