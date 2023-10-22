"""
Estruturas de dados em Python

Tuplas

Tuplas são bastante semelhantes a listas, ou seja, são indexáveis, iteráveis e armazeram qualquer tipo de dados. A principal diferença é que tuplas são imutáveis, ou seja, depois de criadas não podem ter os seus valores alterados.

"""

if __name__ == "__main__":

    # Criação de tuplas
    tupla = ("Python", "Javascript", "C#",)
    print(tupla)
    tupla = tuple("Python")
    print(tupla)

    # Como dito, não podemos alterar um valor de uma tupla já criada. A linha abaixo dará erro
    #tupla[2] = "Golang

    # Caso mesmo assim seja necessário alterar o valor de uma tupla, podemos utilizar a seguinte estratégia:

    # Criamos uma nova lista a partir da tupla
    lista = list(tupla)

    # Alteramos o item desejado
    lista[2] = "Golang"

    # Convertemos novamente a lista em uma tupla
    tupla = tuple(lista)

    print(tupla)