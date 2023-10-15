"""
Match Case

Match Case pode ser entendida como a estrutura switch case no python. Ela é usada quando queremos escolher um valor
dentre valores possíveis.

"""

USUARIO = 1
MODERADOR = 2
ADMINISTRADOR = 3

if __name__ == "__main__":
    
    valor = int(input("Informe a permissão do usuário: "))

    match valor:
        case 1:
            print("Identificado como Usuário. Permissões comuns.")

        case 2:
            print("Identificado como Moderador. Você pode moderar mensagens e usuários.")

        case 3:
            print("Identificado como Administrador. Você possui acesso total.")

        # Caso padrão. Se nenhuma das comparações anteriores retornarem True
        case _:
            print("Permissão desconhecida. Sem informações.")
