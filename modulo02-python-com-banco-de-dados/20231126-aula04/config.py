# config.py
# Arquivos com as configurações do SQLAlchemy

# create_engine é a função que irá criar uma conexão com banco de dados
from sqlalchemy import create_engine

# É a partir da função declarative_base, que vamos criar a classe Base das nossas models. Model significa a classe que está associada a uma tabela no banco de dados.
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker é a função que irá criar a sessão de acesso ao banco de dados. Podemos ter mais de 1 sessão ativa, ou pra bancos de dados diferentes
from sqlalchemy.orm import sessionmaker

# Abaixo está a string de conexão ao banco de dados.
connection_string = "sqlite:///db.sqlite3"

# Abaixo criamos o objeto que representa a conexão ao banco de dados. O primeiro argumento é a connection_string, o argumento echo indica se os comandos SQL que serão executados, serão mostrados no terminal.
conexao = create_engine(connection_string, echo=True)

# Base é a classe de onde todas as models que criarmos serão herdadas. Quaisquer classes que criarmos que não herdar de Base, não terá uma tabela correspondente.
Base = declarative_base()

# Na linha abaixo estamos criando uma sessão de acesso ao banco de dados, que é representado pelo objeto conexao. Ou seja, qualquer comando que executar nessa sessão será executado no banco de dados representado pelo objeto conexao
Session = sessionmaker(bind=conexao)
sessao = Session()