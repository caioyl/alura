# Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram, mostrando os meses por extenso: Janeiro, Fevereiro, etc.
meses = {'Janeiro':0, 'Fevereiro':0,'Março':0,'Abril':0, 'Maio':0, 'Junho':0,'Julho':0, 'Agosto':0, 'Setembro':0, 'Outubro':0, 'Novembro':0, 'Dezembro':0}
temperatura = 0
temperaturas = 0
for chaves in meses.keys():
  temperatura = int(input(f'Digite, em graus Celsius, a temperatura média do mês de {chaves}: '))
  meses[chaves] = temperatura
  temperaturas += temperatura
media = temperaturas/len(meses)
print(f'Valores acima da média {media}:')
for chaves, valores in meses.items():
  if valores > media:
    print(f'{chaves}, com temperatura média de {valores}ºC.')
#Resultado
print('Temperaturas acima da média em: ')
for i in range(0,12):
  # Verificamos todas as temperaturas de acordo com a média anual
  if temperaturas_mensais[i] > media_anual:
    # Como os índices dos meses correspondem às temperaturas,
    # podemos imprimir eles sob o mesmo índice
    print(meses[i])