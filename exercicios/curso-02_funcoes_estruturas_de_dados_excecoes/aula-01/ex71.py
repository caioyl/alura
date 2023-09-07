# Você recebeu uma demanda para gerar números de token para o acesos ao aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
from random import randint
nome = input('Digite seu nome: ')
print(f'Olá, {nome}, o seu token de acesso é {randint(1000,9998)}! Seja bem-vindo(a)!')