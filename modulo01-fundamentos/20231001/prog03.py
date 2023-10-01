# Variáveis e tipos de dados
# Tipos numéricos (int e float)

if __name__ == "__main__":
    numero1 = input("Informe o primeiro número: ")
    numero2 = input("Informe o segundo número: ")

    print("A soma de " + numero1 + " e " + numero2 + " é igual a " + numero1 + numero2)

    """
    No caso acima, o valor da soma de numero1 (10) e numero2 (5) deu 105, pois como vimos anteriormente, o valor
    que a função input() retorna é sempre um tipo texto, ou seja, na verdade estamos concatenando as strings
    10 e 5, resultando em 105.
    Primeiro temos que converter esse tipo texto em um tipo numérico, depois fazemos a operação de soma.
    Podemos converter uma string válida em um número utilizando as funções int() ou float()
    """

    # Aqui, atribuimos os novos valores as variáveis utilizando a função int(), que irá converter
    # um valor string para um valor inteiro
    numero1 = int(numero1)
    numero2 = int(numero2)

    # Utilizamos o método format() de strings, que substitui as chaves ({}) pelos argumentos
    # passados para o método, na ordem em que são informados.
    print("A soma de {} e {} é igual a {}".format(numero1, numero2, numero1 + numero2))

    # --- tipo float()

    # No código abaixo, o valor que é retornado da função input() já é imediatamente convertido
    # para um tipo de dado float, e depois o valor que função float retorna é atribuído às variáveis
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    # Como o operador divisão (/) tem precedência sobre o operador soma (+), utilizamos os parêntesis para
    # indicar que as operações de soma devem ser realizadas antes da operação de divisão.
    # O parêntesis tem precedência sobre quaisquer outros operadores.
    media = (nota1 + nota2 + nota3) / 3

    # Podemos formatar o valor de saída dos números, nos casos onde existam muitos caracteres como casas
    # decimais. Para isso, utilizamos a sintaxe especial de formatação.
    # :.2f significa que após o ponto, vão ser mostradas no máximo 2 casas decimais
    print("A média final é de {:.2f}".format(media))