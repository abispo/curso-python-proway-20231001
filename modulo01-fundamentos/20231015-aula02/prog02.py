"""
Estruturas de repetição

Laço for
* O `for` geralmente é utilizado para percorrer uma sequência (ou container). Ou seja, ele será executado enquanto houverem itens a serem processados. Pode ser entendido como o `for each` em outras linguagens. 

"""

if __name__ == "__main__":

    # A estrutura de dados abaixo é uma lista.
    # Uma lista pode armazenar valores de qualquer tipo
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Utilizando o laço for para mostrar o quadrado de cada número da lista
    for numero in lista_numeros:
        # Abaixo estamos utilizando uma f-string
        # Dentro das chaves colocamos as variáveis que serão utilizadas. Também podemos colocar qualquer expressão válida em Python
        # Também conhecido como interpolação de strings.
        print(f"O quadrado de {numero} é igual a {numero * numero}")

    
    # A estrutura de dados abaixo é uma tupla
    # Ela é muito semelhante a listas, e pode ser passada para o laço for
    tupla_multiplicar = ((3, 4,), (4, 7,), (5, 2,), (8, 3,), (9, 5,))

    # Utilizando o laço for para multiplicar os valores da tupla
    for tupla in tupla_multiplicar:
        numero1, numero2 = tupla
        print(f"{numero1} * {numero2} = {numero1 * numero2}.")

    # Dentro do laço for, podemos utilizar 2 comandos: break e continue

    # break
    # Dentro de um for loop, se for encontrado o comando break, o loop é finalizado automaticamente, independentemente de existirem mais itens a serem lidos.

    # Exemplo: Caso seja encontrado um valor False dentro da lista, o loop é interrompido automaticamente
    lista_acertos = [True, True, True, False, True]

    for acerto in lista_acertos:
        if not acerto:
            print("Existe um erro. Finalizando...")
            break


    # continue
    # Dentro de um for loop, se for encontrado o comando continue, a iteração atual do loop é finalizada, independentemente de haver mais código a ser executado, e passa para a próxima iteração

    # Exemplo: Dada uma lista de notas, vamos mostrar uma mensagem sempre que uma nota for menor do que 4

    lista_notas = [4.5, 4.7, 3.8, 3.9, 4.0, 4.6, 4.6, 3.8, 4.1, 4.2]
    notas_fora_da_media = 0
    media = 0
    soma = 0

    for nota in lista_notas:
        if nota < 4:
            notas_fora_da_media += 1
            print(f"A nota {nota} não entrará para o cálculo da média.")
            continue

        soma += nota

    # A função built-in len(), retorna a quantidade de itens em uma sequência
    # Funções built-in são funções que podemos utilizar sem a necessidade de importar algum pacote, ou seja, são funções carregadas automaticamente pelo interpretador.
    media = soma / (len(lista_notas) - notas_fora_da_media)
    print(f"A média é igual a {media:.2f}.")


    # Apesar de não muito comum, podemos utilizar else dentro do laço for. O bloco else é executado quando o laço for finaliza. Caso um comando break seja executado, o bloco else não é executado

    lista_linguagens = ["Python", "C#", "PHP", "Java"]

    for linguagem in lista_linguagens:

        if linguagem == "Java":
            print(f"{linguagem} não permitida")
            break

    else:
        print("Finalizando leitura de linguagens")