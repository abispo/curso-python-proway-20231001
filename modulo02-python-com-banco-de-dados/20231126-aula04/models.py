# models.py

# Arquivos que irá armazenar as models do sistema

# Classe base das nossas models
from config import Base

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text

class Usuario(Base):
    
    # __tablename__ indica o nome que a tabela terá no banco de dados
    __tablename__ = "tb_usuarios"

    # id será uma coluna do tipo INT, chave primária e auto incremento
    id = Column(Integer, primary_key=True, autoincrement=True)

    # email, senha e nome_usuario serão colunas do tipo varchar(200), que não aceitam valores nulos
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)
    nome_usuario = Column(String(200), nullable=False)


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    data_de_nascimento = Column(Date)


class Postagem(Base):

    __tablename__ = "tb_postagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    corpo = Column(Text)


class Categoria(Base):

    __tablename__ = "tb_categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)