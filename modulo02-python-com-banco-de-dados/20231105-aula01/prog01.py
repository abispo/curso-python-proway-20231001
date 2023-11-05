"""
Python com Banco de Dados

Utilizando um conector para trabalhar com banco de dados SQLite.

Quando usamos os conectores diretamente, temos que informar o comando SQL que será enviado para o banco de dados e que será posteriormente executado.

"""

import os

# O módulo sqlite3 nos permite trabalhar com bancos de dados SQLite. Um banco de dados SQLite é representado por um único arquivo de banco de dados. Esse módulo vem na biblioteca padrão do Python.
import sqlite3

"""
O termo 'connection string' se refere a string de configuração de acesso a um banco de dados. Por exemplo, se fôssemos conectar em um banco de dados MySQL, a connection string deveria ser no formato a seguir:

mysql://<usuario>:<senha>@<endereco_do_servidor>:<porta>/<nome_do_banco_de_dados>

No caso de banco de dados SQLite, precisamos passar o nome do arquivo ou o caminho completo até ele. Lembrano que será criado um arquivo.
"""
connection_string = os.path.join(os.getcwd(), "db.sqlite3")

# Conectando no banco de dados SQLite. Se o banco de dados(arquivo) não existir, ele será criado.
conexao = sqlite3.connect(connection_string)

if __name__ == "__main__":

    # Exclui a tabela tb_estados se ela existir.
    comando = "DROP TABLE IF EXISTS tb_estados;"

    # Criamos um cursor. O cursor é necessário para executar os comandos SQL no banco de dados, assim como para receber os resultados das consultas. Criamos o cursor a partir do objeto de conexão ao banco de dados.
    cursor = conexao.cursor()

    # Executando o comando
    cursor.execute(comando)

    # Definindo o comando de criação da tabela tb_estados
    comando = """
    CREATE TABLE tb_estados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL
    );
    """

    cursor.execute(comando)

    {
    "UF": [
        {"nome": "Acre", "sigla": "AC"},
        {"nome": "Alagoas", "sigla": "AL"},
        {"nome": "Amapá", "sigla": "AP"},
        {"nome": "Amazonas", "sigla": "AM"},
        {"nome": "Bahia", "sigla": "BA"},
        {"nome": "Ceará", "sigla": "CE"},
        {"nome": "Distrito Federal", "sigla": "DF"},
        {"nome": "Espírito Santo", "sigla": "ES"},
        {"nome": "Goiás", "sigla": "GO"},
        {"nome": "Maranhão", "sigla": "MA"},
        {"nome": "Mato Grosso", "sigla": "MT"},
        {"nome": "Mato Grosso do Sul", "sigla": "MS"},
        {"nome": "Minas Gerais", "sigla": "MG"},
        {"nome": "Pará", "sigla": "PA"},
        {"nome": "Paraíba", "sigla": "PB"},
        {"nome": "Paraná", "sigla": "PR"},
        {"nome": "Pernambuco", "sigla": "PE"},
        {"nome": "Piauí", "sigla": "PI"},
        {"nome": "Rio de Janeiro", "sigla": "RJ"},
        {"nome": "Rio Grande do Norte", "sigla": "RN"},
        {"nome": "Rio Grande do Sul", "sigla": "RS"},
        {"nome": "Rondônia", "sigla": "RO"},
        {"nome": "Roraima", "sigla": "RR"},
        {"nome": "Santa Catarina", "sigla": "SC"},
        {"nome": "São Paulo", "sigla": "SP"},
        {"nome": "Sergipe", "sigla": "SE"},
        {"nome": "Tocantins", "sigla": "TO"}
    ]
}