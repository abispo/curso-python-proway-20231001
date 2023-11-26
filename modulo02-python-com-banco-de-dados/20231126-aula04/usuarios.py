import csv
from datetime import date, datetime
import os

from config import sessao

from models import Usuario, Perfil

# Função para criação de usuário
def criar_usuario(email, senha, nome_usuario, nome, data_de_nascimento=None):

    # Primeiro instanciamos a model Usuario, passando os valores para os parâmetros obrigatórios
    usuario = Usuario(
        email=email,
        senha=senha,
        nome_usuario=nome_usuario
    )

    # Adicionamos a instância de Usuario ao objeto sessão. Nesse momento os dados ainda não foram salvos na tabela tb_usuarios
    sessao.add(usuario)

    # O método commit() confirma a transação, executando os comandos que estão em espera no banco de dados
    sessao.commit()

    criar_perfil(usuario, nome, data_de_nascimento)

    return usuario


def criar_perfil(usuario, nome, data_de_nascimento=None):

    # Instanciar a classe Perfil
    perfil = Perfil(
        id=usuario.id,
        nome=nome
    )

    if data_de_nascimento:
        perfil.data_de_nascimento = datetime.strptime(
            data_de_nascimento, "%Y-%m-%d"
        ).date()

    # Adicionar o objeto instanciado à sessão
    sessao.add(perfil)

    # Confirmar a transação na sessão
    sessao.commit()

    # Retornar o objeto instanciado
    return perfil

def carregar_usuarios(nome_arquivo="usuarios.csv"):
    
    print(f"Carregando dados de usuários do arquivo {nome_arquivo}...")
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", nome_arquivo)

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            usuario = criar_usuario(**linha)
            print(f"Usuario '{usuario.email}' salvo com sucesso.")

def listar_usuarios():
    # Retorna uma lista de instâncias da classe Usuario, sendo cada instância uma linha da tabela tb_usuarios
    usuarios = sessao.query(Usuario).all()

    for usuario in usuarios:
        print(usuario)

        # O método get irá retornar uma instância da classe Perfil de acordo com o valor da chave primária que for informado.
        # perfil = sessao.query(Perfil).get(usuario.id)
        # print(perfil)
        print('-'*50)

if __name__ == "__main__":

    menu = """
    ESCOLHA UMA OPÇÃO:
    ******************
    0 - SAIR
    1 - Listar Usuários
    2 - Inserir novo Usuário
    3 - Atualizar um Usuário
    4 - Apagar um Usuário
    5 - Carregar arquivo de usuários"""

    while True:
        print(menu)
        opcao = int(input("Escolha a sua opção: "))

        match opcao:
            case 0:
                break

            case 1:
                listar_usuarios()
            
            case 2 | 3 | 4:
                pass

            case 5:
                nome_arquivo = input("Informe o nome do arquivo: ")
                carregar_usuarios(nome_arquivo) if nome_arquivo else carregar_usuarios()