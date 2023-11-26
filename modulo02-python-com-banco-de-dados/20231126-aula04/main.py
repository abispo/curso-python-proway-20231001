
from config import conexao, Base

from models import *

if __name__ == "__main__":

    # Cria as tabelas que não foram criadas no banco
    Base.metadata.create_all(conexao)