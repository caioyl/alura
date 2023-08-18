# Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a colônia B com 10 elementos.
colonia_A = 4
colonia_B = 10
taxa_A = 0.03
taxa_B = 0.015
dias = 0
while colonia_A <= colonia_B:
  colonia_A *= 1 + taxa_A
  colonia_B *= 1 + taxa_B
  dias += 1
print(f'Serão necessários {dias} dias para a colônia A ultrapassar a colônia B.')