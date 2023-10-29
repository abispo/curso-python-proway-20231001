"""
Funções lambda

Funções lambda também são conhecidas como funções anônimas, ou seja, função que não possuem nome. Geralmente criamos funções lambda quando utilizamos as funções map(), filter() ou reduce()

"""

from random import randint

# Função comum que retorna se o número é par ou não
def e_par(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    
    # Criar uma lista de 100 números inteiros aleatórios de 1 até 100
    lista_numeros = [randint(1, 100) for _ in range(1, 101)]

    # Criar uma lista apenas com os números pares. Para isso, vamos utilizar a função filter()
    # A função filter() filtra os valores de uma sequência, retornando um objeto gerador

    # Chamar o filter passando a função e_par
    # lista_pares = list(filter(e_par, lista_numeros))

    # Chamar o filter passando uma função anônima
    lista_pares = list(filter(lambda x: not x % 2, lista_numeros))

    lista_pares.sort()
    print(lista_pares)

    # Criar uma lista dos quadrados dos números da lista anterior
    # Utilizar a função map() para gerar uma lista de quadrados
    lista_quadrados = list(map(lambda numero: numero * numero, lista_pares))
    print(lista_quadrados)