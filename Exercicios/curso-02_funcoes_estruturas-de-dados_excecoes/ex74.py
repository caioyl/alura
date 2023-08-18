# Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
from math import pi, pow
valor_do_m2 = 25.00
raio = float(input('Digite o raio da área circular em metros: '))
area = pi * pow(raio,2)
preco_a_pagar = round(area*valor_do_m2)
print(f'Você deverá pagar R${round(preco_a_pagar,2)} por uma área de {round(area,2)}m2.')
