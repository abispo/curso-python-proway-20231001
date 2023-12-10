"""
Script que carrega os dados de pedidos de um arquivo .csv e salva nas tabelas tb_pedidos e tb_produtos_pedidos
"""

import csv
import os

from datetime import datetime

from config import sessao
from models import Usuario, Perfil

if __name__ == "__main__":

    try:
        nome_arquivo = input("Informe o nome do arquivo de pedidos(ENTER para carregar o padrão pedidos.csv): ")

        if not nome_arquivo:
            nome_arquivo = "pedidos.csv"

        caminho_arquivo = os.path.join(os.getcwd(), "arquivos", nome_arquivo)

        with open(file=caminho_arquivo, mode='r', encoding="utf-8") as arquivo:

            arquivo_csv = csv.DictReader(arquivo, delimiter=';')

            for linha in arquivo_csv:
                pass

            sessao.commit()

    except Exception as exc_info:
        print(f"Erro ao carregar o arquivo: {exc_info}.")