"""
Funções recursivas

São funções que chamam a si mesmas

Exemplo de onde pode ser aplicada uma função recursiva: Cálculo do fatorial de um número

5! = 5 * 4 * 3 * 2 * 1      = 120
3! = 3 * 2 * 1              = 6
6! = 6 * 5 * 4 * 3 * 2 * 1  = 720

"""

def fatorial_nao_recursivo(numero):
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador = contador - 1

    return total


def fatorial_recursivo(numero):
    if numero == 1:
        return numero
     
    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":
    print(fatorial_nao_recursivo(6))
    print(fatorial_recursivo(10))