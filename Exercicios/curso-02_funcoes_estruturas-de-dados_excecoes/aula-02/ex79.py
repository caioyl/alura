# Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram.
# Retorne a média para apresentar o texto:
# "Nota da manobra: [media]"

# Declarando a lista de notas
notas = []

# Lendo as notas e adicionando à lista
for c in range(1,6):
  nota = float(input(f'Digite a {c}ª nota: '))
  notas.append(nota)

# Definindo a função
def pontuacao(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  media = sum(lista) / len(lista)
  return media

# Chamando a função e imprimindo a nota
media = pontuacao(notas)
print(f'Nota da manobra: {round(media,1)}')