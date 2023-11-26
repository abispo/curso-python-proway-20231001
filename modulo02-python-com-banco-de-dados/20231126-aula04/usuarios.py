from config import sessao

from models import Usuario, Perfil

# Função para criação de usuário
def criar_usuario(email, senha, nome_usuario, nome, data_de_nascimento):

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


def criar_perfil(usuario, nome, data_de_nascimento):

    # Instanciar a classe Perfil
    perfil = Perfil(
        id=usuario.id,
        nome=nome,
        data_de_nascimento=data_de_nascimento
    )

    # Adicionar o objeto instanciado à sessão
    sessao.add(perfil)

    # Confirmar a transação na sessão
    sessao.commit()

    # Retornar o objeto instanciado
    return perfil

if __name__ == "__main__":
    pass