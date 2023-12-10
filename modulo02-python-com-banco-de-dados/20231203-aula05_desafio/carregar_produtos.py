"""
Script que carrega os dados de clientes de um arquivo .csv e salva nas tabelas tb_usuarios e tb_perfis
"""

import csv
import os

from config import sessao
from models import Produto

if __name__ == "__main__":

    try:
        nome_arquivo = input("Informe o nome do arquivo de produtos(ENTER para carregar o padrão produtos.csv): ")

        if not nome_arquivo:
            nome_arquivo = "produtos.csv"

        caminho_arquivo = os.path.join(os.getcwd(), "arquivos", nome_arquivo)

        with open(file=caminho_arquivo, mode='r', encoding="utf-8") as arquivo:

            arquivo_csv = csv.DictReader(arquivo, delimiter=';')

            for linha in arquivo_csv:
                
                produto = Produto(**linha)
                sessao.add(produto)

            sessao.commit()

    except Exception as exc_info:
        print(f"Erro ao carregar o arquivo: {exc_info}.")