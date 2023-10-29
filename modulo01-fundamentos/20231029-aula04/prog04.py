"""
Trabalhando com arquivo .csv no Python

Escrita de arquivos .csv com writer e DictWriter

CSV -> Comma-Separated Values -> Valores Separados por Vírgula
"""

# Módulo do Python para se trabalhar com arquivos .csv
import csv

# O módulo os do Python permite trabalhar com algumas coisas relacionadas ao sistema operacional, como caminho de pastas, checagem de tipos de arquivos, etc.
import os

# os.getcwd()   -> Retorna o caminho completo da pasta onde o script está sendo executado
pasta_arquivos = os.path.join(os.getcwd(), "arquivos")

if __name__ == "__main__":
    
    # Trabalhando com writer

    lista_clientes = [
        ["Maria", "20", "600.45"],
        ["José", "38", "567"],
        ["João", "21", "345.86"]
    ]

    with open(os.path.join(pasta_arquivos, "clientes.csv"), "w", encoding="utf-8", newline="") as arquivo:

        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # Salvar o nome das colunas com writerow()
        arquivo_csv.writerow(["nome", "idade", "valor"])

        # Salvar os dados ds clientes com writerows()
        arquivo_csv.writerows(lista_clientes)


    # Trabalhando com DictWriter

    lista_acessos = [
        {"nome": "Maria", "ultimo_acesso": "20231001"},
        {"nome": "Sandra", "ultimo_acesso": "20231002"},
        {"nome": "Roberto", "ultimo_acesso": "20231011"},
        {"nome": "Carlos", "ultimo_acesso": "20231011"},
        {"nome": "José", "ultimo_acesso": "20231020"},
    ]

    with open(os.path.join(pasta_arquivos, "acessos.csv"), "w", newline="", encoding="utf-8") as arquivo:

        nomes_colunas = ["nome", "ultimo_acesso"]
        arquivo_csv = csv.DictWriter(arquivo, fieldnames=nomes_colunas, delimiter=';')

        # Podemos utilizar o método writeheader para salvar a primeira linha como as colunas
        arquivo_csv.writeheader()

        # Salvar uma linha no arquivo
        arquivo_csv.writerow({"nome": "Valdir", "ultimo_acesso": "20231014"})

        # Salvar uma lista de registros no arquivo
        arquivo_csv.writerows(lista_acessos)