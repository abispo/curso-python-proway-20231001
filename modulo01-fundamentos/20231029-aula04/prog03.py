"""
Trabalhando com arquivo .csv no Python

Leitura de arquivos .csv com reader e DictReader

CSV -> Comma-Separated Values -> Valores Separados por Vírgula
"""

# Módulo do Python para se trabalhar com arquivos .csv
import csv

# O módulo os do Python permite trabalhar com algumas coisas relacionadas ao sistema operacional, como caminho de pastas, checagem de tipos de arquivos, etc.
import os

# os.getcwd()   -> Retorna o caminho completo da pasta onde o script está sendo executado
pasta_arquivos = os.path.join(os.getcwd(), "arquivos")

# Função que calcula a média das notas
def calcula_media(nome, n1, n2, n3, n4, n5):
    media = (float(n1) + float(n2) + float(n3) + float(n4) + float(n5)) / 5
    return f"O(a) Aluno(a) {nome} possui a média {media:.1f}."

if __name__ == "__main__":

    # Utilizando csv.reader

    # Primeiro passo: Abrir o arquivo
    # Aqui concatenamos o caminho da pasta 'arquivos' com o arquivo 'notas.csv'. Dessa maneira passamos o caminho completo para a abertura do arquivo.
    with open(os.path.join(pasta_arquivos, "notas.csv"), "r", encoding="utf-8") as arquivo:

        # Segundo passo: Criar um objeto do tipo arquivo csv
        # Por padrão, o módulo csv considera que o caractere separador dos dados é a vírgula. Como nosso arquivo utiliza o ponto-e-vírgula como separador, precisamos indicar isso para a função reader.
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            if linha[0] != "nome":
                print(calcula_media(*linha))

        # A função reader do módulo CSV, retorna cada linha do arquivo csv como uma lista de valores, que foram separados pelo delimitador

    print('-'*100)

    # Utilizando o DictReader

    # Primeiro passo: Abrir o arquivo
    with open(os.path.join(pasta_arquivos, "notas.csv"), "r", encoding="utf-8") as arquivo:

        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            print(calcula_media(**linha))