# Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.
# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".".
# Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.
# Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if (Por exemplo, ('a' or 'b') in 'alura' ... Saída: True)
# Os dados para o teste do código são:
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

def verificar_se_foi_tratado(lista):
  for i in range(len(lista)):
    if (',' or '.' or '!' or '?') in lista[i]:
      raise ValueError(f"O texto apresenta pontuações na palavra '{lista[i]}'")
  print('A lista foi tratada')
verificar_se_foi_tratado(lista_nao_tratada)
