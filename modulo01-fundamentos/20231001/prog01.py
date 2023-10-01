
# Toda linha que começar com '#', é considerada comentário e será ignorada pelo interpretador do Python

# Apesar de não ser necessário para rodar os script Python, é considerada uma boa prática verificarmos se o script
# está sendo chamado diretamente pelo interpretador. Essa checagem é feita utilizando a estrutura abaixo:
# Se o valor da variável '__name__' for igual a '__main__', o código dentro do bloco if será executado
# Também podemos chamar isso de 'entrypoint' da aplicação.
if __name__ == "__main__":

    # Imprime a mensagem 'Olá mundo!' no terminal
    print("Olá mundo!")

    # A identação do código faz parte da sintaxe válida da linguagem Python. Sempre que iniciarmos
    # um novo bloco de código, devemos inserir um espaço de 4 caracteres a partir da primeira
    # linha do bloco de código.
    # Um bloco de código sempre é criado quando uma linha termina com 2 pontos (:)
    #     print("Essa linha não será executada pois a identação é diferente da primeira linha do bloco")
