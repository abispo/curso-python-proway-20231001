"""
Estruturas de dados em Python

Dicionários (dict)

Um dicionário é uma estrutura de dados no formato {chave: valor}, que é ordenado, mutável, iterável e que não permite chaves repetidas.

"""

if __name__ == "__main__":

    # Podemos criar dicionário de 2 maneiras:

    dicio1 = {}                                     # Dicionário vazio
    dicio1 = dict()

    dicio2 = {"curso": "Python", "sala": "Blue"}    # Dicionário já preenchido
    dicio2 = dict(curso="Python", sala="Blue")

    print(dicio1, dicio2)

    # Não há problemas em termos valores repetidos nos dicionários, o que não é possível ter são chaves
    # repetidas e tipos de chaves diferentes de string, numeros ou booleanos

    # Exemplo: A linha abaixo irá gerar uma exceção, pois não podemos ter listas como chaves de dicionários
    # erro = {[1, 2, 3]: "Impossível"}

    # De preferência, sempre utilize strings como chaves de dicionários.

    # Exemplo de dicionário

    usuario = {
        "id": 10,
        "score": 7.5,
        "tipo": ["redator"],
        "info": {
            "nome": "José",
            "setor": 14,
            "nível": 2
        },
        "ativo": True
    }

    print(usuario)

    # Então, percebe-se que poemos ter quaisquer tipos de dados como valores de um dicionário, inclusive lista
    # e outros dicionários.

    # Acessando um valor do dicionário.

    # Podemos passar o nome da chave entre colchetes
    print(usuario["info"])

    # Caso a chave não exista, recebemos uma exceção do tipo KeyError
    # print(usuario["cidade"])

    # Para evitar ser gerada uma exceção(erro) do tipo KeyError caso a chave do dicionário não exista, podemos utilizar 2 saídas:

    # 1 - Utilizar o método get, que retorna None ou um valor padrão caso a chave não exista
    print(usuario.get("cidade"))

    # Retornando um texto padrão ao invés de None
    print(usuario.get("cidade", "A chave 'cidade' não existe."))

    # 2 - Capturar a exceção e tratá-la

    try:
        print(usuario["cidade"])

    except KeyError:
        print("A chave 'cidade' não existe no dicionário usuario.")


    # Assim como listas, dicionários também são objetos iteráveis, ou seja, podemos acessar os seus itens de maneira sequencial dentro de um loop

    print("-"*100)

    for chave in usuario:
        print(chave)

    # Por padrão, quando utilizamos a sintaxe acima, é executado o método keys() do dicionário, que retorna a lista das chaves. Existem 3 métodos que retorna informações sobre os itens de um dicionário, que são os seguintes:

    print(f"Retornando apenas as chaves com o método keys(): {usuario.keys()}")
    print(f"Retornando apenas os valores com o método values(): {usuario.values()}")
    print(f"Retornando uma lista de tuplas chave, valor com o método items(): {usuario.items()}")

    # Pegando apenas os valores
    for valor in usuario.values():
        print(valor)

    print('*'*10)

    # Pegando o par chave valor
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")