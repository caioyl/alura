# Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros, sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
doces = amargos = []
for c in range (0,9):
  ID = int(input('Digite a ID do produto: '))
  if ID % 2 == 0:
    doces.append(ID)
  else:
    amargos.append(ID)
print(f'A quantidade de produtos doces é igual a: {len(doces)}.\nSão eles: {doces}.\nA quantidade de produtos amargos é igual a: {len(amargos)}.\nSão eles: {amargos}.')