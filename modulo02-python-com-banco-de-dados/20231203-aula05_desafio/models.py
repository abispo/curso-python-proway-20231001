
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from config import Base


class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)

    perfil = relationship("Perfil", back_populates="usuario", uselist=False)


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(200), nullable=False)
    telefone = Column(String(20), nullable=True)
    data_de_nascimento = Column(DateTime, nullable=True)
    genero = Column(String(20), nullable=True)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)


class Produto(Base):

    __tablename__ = "tb_produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String(36), nullable=False)
    nome = Column(String(200), nullable=False)
    descricao = Column(String(500), nullable=False)
    preco_unitario = Column(Float, nullable=False)
