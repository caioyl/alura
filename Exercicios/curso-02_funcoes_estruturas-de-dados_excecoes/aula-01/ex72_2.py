# Para diversificar e atrair novos clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salade de frutas da pessoa cliente
from random import choices, choice
frutas = ["maçã", "banana", "uva", "pêra",
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
salada_de_frutas = []
for c in range(0,3):
  fruta_selecionada = choice(frutas)
  salada_de_frutas.append(fruta_selecionada)
  frutas.remove(fruta_selecionada)
print(salada_de_frutas)
