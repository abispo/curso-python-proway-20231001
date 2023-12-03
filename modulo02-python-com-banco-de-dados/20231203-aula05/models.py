# models.py

# Arquivos que irá armazenar as models do sistema

# Classe base das nossas models
from config import Base

from sqlalchemy import Column, DateTime, Integer, String, Date, ForeignKey, Text, Table, func

from sqlalchemy.orm import relationship

postagens_categorias = Table(
    "tb_postagens_categorias",
    Base.metadata,
    Column("postagem_id", Integer, ForeignKey("tb_postagens.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("tb_categorias.id"), primary_key=True)
)

class Teste:
    pass

class Usuario(Base):
    
    # __tablename__ indica o nome que a tabela terá no banco de dados
    __tablename__ = "tb_usuarios"

    # id será uma coluna do tipo INT, chave primária e auto incremento
    id = Column(Integer, primary_key=True, autoincrement=True)

    # email, senha e nome_usuario serão colunas do tipo varchar(200), que não aceitam valores nulos
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())
    atualizado_em = Column(DateTime, onupdate=func.now())

    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    postagens = relationship("Postagem", back_populates="usuario")

    def __str__(self):
        return f"Usuario<email={self.email}, nome={self.perfil.nome}>"


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(200), nullable=False)
    data_de_nascimento = Column(Date)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)

    def __str__(self):
        data_nascimento = self.data_de_nascimento

        if data_nascimento:
            data_nascimento = self.data_de_nascimento.strftime('%d/%m/%Y')
        
        return f"Perfil<nome='{self.nome}', data_de_nascimento='{data_nascimento}'>"


class Postagem(Base):

    __tablename__ = "tb_postagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    corpo = Column(Text)

    usuario = relationship("Usuario", back_populates="postagens", uselist=False)


class Categoria(Base):

    __tablename__ = "tb_categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)