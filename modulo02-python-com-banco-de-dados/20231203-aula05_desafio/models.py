
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from config import Base


class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(200), nullable=False)
    senha = Column(String(200), nullable=False)

    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    pedidos = relationship("Pedido", back_populates="usuario", uselist=True)


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

    pedidos = relationship("ProdutoPedido", back_populates="produto", uselist=True)


class Pedido(Base):

    __tablename__ = "tb_pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("tb_usuarios.id"), nullable=False)
    data_do_pedido = Column(Date, nullable=False)

    usuario = relationship("Usuario", back_populates="pedidos", uselist=False)
    produtos = relationship("ProdutoPedido", back_populates="pedido", uselist=True)


# Tabela associativa entre produtos e pedidos. Como teremos mais dados além das chaves estrangeiras, é preferível que nesses casos criemos as models da maneira padrão (e não utilizando a classe Table)
class ProdutoPedido(Base):

    __tablename__ = "tb_produtos_pedidos"

    produto_id = Column(Integer, ForeignKey("tb_produtos.id"), primary_key=True)
    pedido_id = Column(Integer, ForeignKey("tb_pedidos.id"), primary_key=True)
    quantidade = Column(Integer, nullable=False)

    produto = relationship("Produto", back_populates="pedidos", uselist=False)
    pedido = relationship("Pedido", back_populates="produtos", uselist=False)
