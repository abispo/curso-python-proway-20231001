"""
Script que carrega os dados de pedidos de um arquivo .csv e salva nas tabelas tb_pedidos e tb_produtos_pedidos
"""

import csv
import os

from datetime import datetime

from config import sessao
from models import Pedido, Produto, Usuario, ProdutoPedido

if __name__ == "__main__":

    try:
        nome_arquivo = input("Informe o nome do arquivo de pedidos(ENTER para carregar o padrão pedidos.csv): ")

        if not nome_arquivo:
            nome_arquivo = "pedidos.csv"

        caminho_arquivo = os.path.join(os.getcwd(), "arquivos", nome_arquivo)

        lista_pedidos = {}

        with open(file=caminho_arquivo, mode='r', encoding="utf-8") as arquivo:

            arquivo_csv = csv.DictReader(arquivo, delimiter=';')

            for linha in arquivo_csv:

                usuario = sessao.query(Usuario).filter_by(email=linha.get("email")).first()

                produto = sessao.query(Produto).filter_by(sku=linha.get("sku")).first()

                pedido_id = linha.get("pedido_id")
                
                data_do_pedido=datetime.strptime(
                    linha.get("data_do_pedido"),
                    "%Y-%m-%d"
                ).date()

                if not pedido_id in lista_pedidos.keys():
                    lista_pedidos[pedido_id] = {
                        "usuario": usuario,
                        "data_do_pedido": data_do_pedido,
                        "produtos": [{
                            "quantidade": int(linha.get("quantidade")),
                            "produto": produto
                        }]
                    }

                else:
                    lista_pedidos[pedido_id]["produtos"].append({
                        "quantidade": int(linha.get("quantidade")),
                        "produto": produto
                    })

        for _, info_pedido in lista_pedidos.items():
            pedido = Pedido(
                usuario=info_pedido.get("usuario"),
                data_do_pedido=info_pedido.get("data_do_pedido")
            )

            for produto in info_pedido.get("produtos"):
                produto_pedido = ProdutoPedido(
                    produto=produto.get("produto"),
                    quantidade=produto.get("quantidade")
                )

                pedido.produtos.append(produto_pedido)

            sessao.add(produto_pedido)
            sessao.add(pedido)

        sessao.commit()

    except Exception as exc_info:
        print(f"Erro ao carregar o arquivo: {exc_info}.")