"""
Estruturas de dados em Python

Sets (conjuntos)

Um set é uma estrutura de ddos que armazena um conjunto de valores. Sets não são ordenados, não são indexáveis, são imutáveis* e não permitem valores repetidos.

* Apesar de não conseguirmos alterar um valor existente, podemos adicionar ou remover valores

"""

from random import randint

if __name__ == "__main__":
    
    # Criação de um set
    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = set([5, 4, 3, 2, 1])

    print(conjunto_a, conjunto_b)

    try:
        # A linha abaixo irá gerar uma exceção do tipo TypeError
        print(conjunto_a[0])

    except TypeError:
        print("Sets não são indexáveis.")


    # Criando a lista de números aleatórios da maneira "clássica"
    lista_numeros = []
    
    # A função range() gerá uma sequência de números. No caso abaixo, de 0 até 98
    for numero in range(100):
        lista_numeros.append(randint(1, 50))

    print(lista_numeros)

    # Criando a lista de números utilizando list comprehension
    # Quando não utilizamos uma variável, mas ela é necessária pra sintaxe da expressão, podemos trocá-la pelo underline (_)
    lista_numeros = [randint(1, 50) for _ in range(100)]
    print(f"Tamanho: {len(lista_numeros)} | ", lista_numeros)

    # Removendo os valores repetidos. Para isso, vamos converter a lista para um set e converter esse set para uma lista.

    lista_numeros = list(set(lista_numeros))
    print(lista_numeros)