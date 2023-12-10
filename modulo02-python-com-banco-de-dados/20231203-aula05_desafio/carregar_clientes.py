"""
Script que carrega os dados de clientes de um arquivo .csv e salva nas tabelas tb_usuarios e tb_perfis
"""

import csv
import os

from datetime import datetime

from config import sessao
from models import Usuario, Perfil

if __name__ == "__main__":

    try:
        nome_arquivo = input("Informe o nome do arquivo de clientes(ENTER para carregar o padrão clientes.csv): ")

        if not nome_arquivo:
            nome_arquivo = "clientes.csv"

        caminho_arquivo = os.path.join(os.getcwd(), "arquivos", nome_arquivo)

        with open(file=caminho_arquivo, mode='r', encoding="utf-8") as arquivo:

            arquivo_csv = csv.DictReader(arquivo, delimiter=';')

            for linha in arquivo_csv:
                
                usuario = Usuario(
                    email=linha.get("email"),
                    senha=linha.get("senha")
                )

                # Converte a string para datetime
                data_de_nascimento = datetime.strptime(
                    linha.get("data_nascimento"),
                    "%Y-%m-%d"
                ).date()

                perfil = Perfil(
                    nome=linha.get("nome"),
                    sobrenome=linha.get("sobrenome"),
                    telefone=linha.get("telefone"),
                    data_de_nascimento=data_de_nascimento,
                    genero=linha.get("genero")
                )

                usuario.perfil = perfil
                sessao.add(usuario)

            sessao.commit()

    except Exception as exc_info:
        print(f"Erro ao carregar o arquivo: {exc_info}.")