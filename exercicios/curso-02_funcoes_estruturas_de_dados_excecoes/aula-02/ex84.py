# Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres
# Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter()recebe uma função no nosso exemplo uma função lambda e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.
# Use a frase Aprender Python aqui na Alura é muito bom para testar o código.

#Lendo a frase
frase = input('Toda frase digitada será retornada com suas palavras com 5 letras ou mais.\n\nDigite a frase a ser filtrada: ')

#Tratando a frase, transformando-a em uma lista
frase_filtrada = frase.replace('.',' ').replace(',',' ').replace('!','').replace('?',' ').split() #split() transforma cada elemento de uma string (seprarados naturalmente por espaço) em um elemento string de uma lista

#Filtrando a frase
frase_final = list(filter(lambda x: len(x) >= 5, frase_filtrada))
print(frase_final)
