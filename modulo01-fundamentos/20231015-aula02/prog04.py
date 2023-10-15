"""
Estruturas de dados em Python

Lista

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