# Como cientista de dados em um time e futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.
# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas lista de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
# Observação: Se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.
# Para teste, utilize as seguintes listas de gols marcados e sofridos:
# gols_marcados = [2, 1, 3, 1, 0]
# gols_sofridos = [1, 2, 2, 1, 3]
#Listas dos gols marcados e sofridos
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

#Definição da função que calcula os pontos
def calcula_pontos(gols_marcados, gols_sofridos):
   pontuacao = 0
   #Criando um laço para iterar cada um dos gols de acordo com cada jogo
   for i in range (0,len(gols_marcados)):
      gols_feitos = gols_marcados[i]
      gols_levados = gols_sofridos[i]
    #Definindo o resultado
      #Vitória
      if gols_feitos > gols_levados:
         pontuacao += 3
      #Empate
      if gols_feitos == gols_levados:
         pontuacao += 1
      #Derrota não agrega pontos, então não precisa ser declarado
  #Cálculo do aproveitamento
   aproveitamento = round((pontuacao/ (len(gols_marcados) * 3))* 100,1)
   return pontuacao, aproveitamento

#Inserindo o valor retornado pela função nas variáveis pontuação e aproveitamento
pontuacao, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
#Lendo os valores
print(f'A pontuação do time foi de {pontuacao} e seu aproveitamento foi de {aproveitamento}%')
