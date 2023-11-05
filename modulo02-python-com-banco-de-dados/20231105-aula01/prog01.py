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

    lista_estados = [
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

    for estado in lista_estados:

        nome = estado.get("nome")
        sigla = estado.get("sigla")

        # Montar o comando de inserção
        comando = f"INSERT INTO tb_estados(nome, sigla) VALUES ('{nome}', '{sigla}');"

        # Executar o comando
        cursor.execute(comando)

        # Precisamos confirmar a transação utilizando o método commit()
        conexao.commit()

        print(f"Estado '{nome}' inserido com sucesso.")

    # Ou então executamos o commit() ao final do loop, os dados serão inseridos todos de uma vez
    # conexao.commit()

    print(f"{'*'*49} CONSULTA DE DADOS {'*'*49}")
    # Visualizando os dados da tabela tb_estados

    # Criamos o comando de consulta
    comando = "SELECT * FROM tb_estados"

    # Executando a consulta 
    resultado = cursor.execute(comando)

    # Podemos trazer os dados utilizando 3 métodos diferentes
    # O método fetchone() trás apenas o primeiro resultado da consulta
    # print(resultado.fetchone())

    # O método fetchmany(numero) trás a quantidade de registros indicado no parâmetro numero
    # print(resultado.fetchmany(10))

    # O método fetchall() trás todos os registros restantes da consulta
    print(resultado.fetchall())

    # É importante notar que, assim como no acesso a arquivos, caso o cursor interno chegue no final da consulta, será necessário executar novamente a consulta pra trazer mais dados. A linha abaixo retornará None, pois não existem mais registros a serem lidos.
    print(resultado.fetchone())

    # Trazendo novamente os dados
    resultado = cursor.execute(comando)

    # Salvando a lista de registros em uma variável
    estados = resultado.fetchall()

    for estado in estados:
        saida = f"""
        Estado: {estado[1]}
        Sigla: {estado[2]}
        -------------------------------------
        """
        print(saida)

    # Fecha a conexão do cursor.
    cursor.close()

    # Fecha a conexão com o banco de dados
    conexao.close()
