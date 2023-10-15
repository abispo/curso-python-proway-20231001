"""
Estruturas de dados em Python

Listas

Uma lista é um dos tipos de estruturas de dados em Python. Ela tem as seguintes características: Ser ordenada, mutável, indexável e permitir valores repetidos.

"""

if __name__ == "__main__":

    # Listas podem ser criadas das seguintes maneiras:

    lista = []                  # Lista vazia
    lista = [1, 2, 3]           # Listá criada com valores
    lista = list()              # Utilizando a função list()
    lista = list("Python")      # Passando um objeto iterável para a lista

    # Listas em Python são ordenadas, ou seja, elas vão manter a ordem dos itens no momento de sua criação
    print(lista)

    # Também são mutáveis, ou seja, podemos alterar qualquer item da lista
    lista[0] = "a"          # Alteramos um valor da lista a partir da posição
    print(lista)

    # Também são indexáveis, ou seja, podemos acessar qualquer valor da lista a partir do valor do índice
    print(lista[3])

    """
    Os índices de uma lista em Python funcionam da seguinte maneira:

    linguagens = ["Python", "C#", "Java", "Javascript", "Golang"]
                     0       1       2          3           4
                    -5      -4      -3         -2          -1
    
                     
    Vimos acima que também podemos utilizar índices negativos na nossa lista, começando do final com -1
    """

    # Pegando a penúltima letra da lista
    print(lista[-2])


    # Por última, uma lista pode ter valores repetidos
    lista = ["Proway", "Blumenau", "Blumenau"]
    print(lista)


    """
    Fatiamento de listas em Python

    Em Python, podemos fazer o 'slicing' (fatiamento) de listas, que nada mais são do que extrairmos pedaços de uma lista, a partir dos seus índices. Note que quando utilizamos o fatiamento, uma nova lista é criada.

    Sintaxe: [start:stop:step]
    
    start (opcional): Índice de início inclusivo
    stop (opcional): Índice de fim exclusivo
    step (opcional): De quantos em quantos itens serão extraídos
    """

    linguagens = ["Python", "C#", "Java", "Javascript", "Golang", "PHP", "SQL", "Perl"]

    # Exemplo: "Fatiar" a lista extraindo os valores "Java" e "Javascript"
    print(linguagens[2:4])

    # Exemplo 2: Pegar todos os itens da lista, pulando de 2 em 2
    print(linguagens[1::2])

    # Exemplo 3: Utilizando índices negativos no slice
    print(linguagens[:-1:2])

    ### Métodos de listas em Python

    ## Métodos de remoção de elementos

    # remove()
    # Remove um item de uma lista a partir do seu valor. Caso exista mais um 1 item com o mesmo valor, a primeira ocorrência encontrada da esquerda para a direita é removida

    linguagens.remove("SQL")
    print(linguagens)


    # pop(indice)
    # Remove e retorna um item de uma lista a partir do índice informado. Se não for informad um índice, retorna o último elemento da lista
    print(f"Removendo '{linguagens.pop(2)}' da lista")
    print(linguagens)


    # Comando del
    # Podemos remover um item da lista utilizando esse comando
    del linguagens[-1]
    print(linguagens)


    # clear()
    # Apaga todos os itens da lista
    linguagens.clear()
    print(linguagens)


    ## Métodos de adição de elementos

    # append(item)
    # Insere um item no final de uma lista
    linguagens.append("Python")
    print(linguagens)

    # extend(sequencia)
    # Extende os itens de uma lista com os itens da sequência informada
    tupla_linguagens = ("C#", "Javascript", "SQL",)
    linguagens.extend(tupla_linguagens)
    print(linguagens)

    # insert(posicao, valor)
    linguagens.insert(-1, "Golang")
    print(linguagens)

    # Também podemos concatenar uma lista com a outra
    linguagens += ["Perl", "Haskell"]
    print(linguagens)