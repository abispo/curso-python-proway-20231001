"""
Entrada e saída de arquivos (File I/O)

Leitura de arquivos .txt no Python

"""

if __name__ == "__main__":

    """
    Para abrir arquivos no Python, utilizamos a função built-in open(). Essa função possui um argumento obrigatório que é o nome/caminho do arquivo a ser aberto. Também podemos passar o modo de abertura.
    """

    """
    Aqui abrimos o arquivos 'linguagens.txt'. É importante notar que, dessa maneira, o arquivo deve estar na mesma pasta que o script que o abre. Caso não exista, recebemos um erro.

    Também podemos passar o modo de abertura do arquivo. Caso não passemos, automaticamente o Python considera que o modo de abertura será o somente-leitura. Podemos utilizar os seguites modos:

    'r'     -> Somente Leitura
    'w'     -> Somente Escrita
    'a'     -> Modo append (abre para escrita mantendo o conteúdo do arquivos)
    'r+'    -> Abre tanto pra leitura quanto para escrita

    Complementar a isso, podemos indicar o tipo de arquivo a ser aberto, como texto plano 't' ou binário 'b'. Exemplo:

    'rb'    -> Abre o arquivo no modo binário somente para leitura.

    """
    arquivo = open("linguagens.txt", mode="r")

    """
    A função read lê o conteúdo do arquivo, e retorna como string. Opcionalmente, podemos indicar a quantidade de caracteres que podemos ler.

    A linha abaixo lê os primeiros 10 caracteres do arquivo
    """
    print(arquivo.read(10))

    # A linha abaixo lê o restante do arquivo
    print(arquivo.read())

    # Sempre devemos fechar o arquivo que abrimos. Essa é uma boa prática que evita o consumo desnecessário de recursos do sistema.
    arquivo.close()

    print('-'*100)

    # O comando with cria um novo contexto de execução. Quando é utilizado em conjunto com a função open() para abrir um arquivo, quando esse contexto é finalizado, o arquivo é fechado automaticamente, não necessitando utilizar o método close()
    with open("linguagens.txt") as arquivo:
        
        # O método readline() lê uma linha inteira do Python, inclusive retornando os caracteres especiais, como \t (TAB) e \n (ENTER).
        print(arquivo.readline())

        # Podemos passar um argumento opcional para o readline, que indica a quantidade de caracteres que queremos ler nessa linha
        print(arquivo.readline(2))

        # O método readlines() lê o conteúdo do arquivo e retorna uma lista, com cada linha desse arquivo sendo um item dessa lista.
        print(arquivo.readlines())

        # Podemos passar um argumento opcional para o readlines, que indica a quantidade de caracteres que queremos ler
        print(arquivo.readlines(10))

        # A linha acima retorna uma lista vazia, pois não há mais caracteres a serem lidos. Internamente o Python cria um cursor no arquivo que será movido a medida que o conteúdo desse arquivo é lido. Para "rebobinarmos" esse cursor, devemos utilizar o método seek, passando a posição desejada.
        arquivo.seek(0)

        # Lê os primeiros 20 caracteres do arquivo
        print(arquivo.readlines(20))