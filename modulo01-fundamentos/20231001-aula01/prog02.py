# Variáveis e tipos de dados
# Strings

if __name__ == "__main__":
    
    # A função input() recebe um valor informado pelo terminal, e retorna esse mesmo valor como um texto
    # Esse valor é atribuído à variável nome
    # '=' é o operador de atribuição igual, que irá atribuir à variável nome o valor do retorno da função
    # input()
    nome = input("Informe o seu nome: ")

    # A função input() retorna um tipo de dado str (string, texto)
    idade = input("Informe a sua idade: ")
    
    print(nome)
    print(idade)

    # Strings em python são cadeias de caractes, que podem ter qualquer tamando. Podem ser usadas
    # 'aspas simples' ou "aspas duplas", não há diferença.

    # Tudo que estiver dentro de aspas simples ou aspas duplas, é uma string (texto)
    mensagem = 'Bem vindo ao Curso de Python'
    print(mensagem)

    mensagem = 'Estamos no "módulo 01 fundamentos"'
    print(mensagem)

    # O python também tem suporte a uma string chamada string multilinhas. Ela começa e termina com 3 aspas

    mensagem = """
    Bem-vindo ao curso de Python da proway. O curso está dividido em 3 módulos:
        1. Fundamentos da Linguagem
        2. Acessando bancos de dados com Python
        3. Python Web com Django Framework

    """

    # Strings multilinha também são normalmente utilizadas para representar comentários multi linha do código.
    print(mensagem)