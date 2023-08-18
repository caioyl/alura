# Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para uma das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é 14km/l, sendo que o valor da gasolina é de 5 reais o litro. Os gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gastos_hotel), 2ª calcule os gastos com a gasolina (gastos_gasolina) e a 3ª os gastos com passeio e alimentacao (gastos_passeio).
# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta e carro.
# Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] e saindo de Recife custaria [gastos] reais
#Definindo as listas
lista_distancias = [850, 800, 300, 550]
hotel = 150
lista_alimentacao_por_dia = [200, 400, 250, 300]

#Calculando as funçõess
def funcao_gasolina(rendimento, distancias):
   gasolina = (distancias * 2 ) / rendimento * 5
   return gasolina

def funcao_hotel(diaria, dias):
   hotel = diaria * dias
   return hotel

def funcao_alimentacao(alimentacao):
   alimentos = alimentacao * dias
   return alimentos

#Lendo os valores
cidade = int(input(f'Salvador [1]\nFortaleza [2]\nNatal [3]\nAracaju [4]\n\nDigite a cidade para qual você irá viajar: '))
dias = int(input('Digite a quantidade de dias: '))

#Inserindo o valor retornado pelas funções nas variáveis de gastos
gastos_gasolina = round(funcao_gasolina(14, lista_distancias[cidade - 1]),2)
gastos_hotel = round(funcao_hotel(150, dias),2)
gastos_alimentacao = round(funcao_alimentacao(lista_alimentacao_por_dia[cidade - 1]),2)
gasto_total = round(gastos_gasolina + gastos_alimentacao + gastos_hotel,2)

#Imprimindo os resultados
print(f'\nO gasto total da viagem será R${gasto_total}. \n\nValores discriminados:\nAlimentação: R${gastos_alimentacao}\nHotel: R${gastos_hotel}\nGasolina: R${gastos_gasolina}')
