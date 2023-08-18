# Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes
#Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado
from random import randint
n_participantes = int(input('Digite o número de participantes: '))
print(f'O número sorteado foi {randint(1, n_participantes)}')
