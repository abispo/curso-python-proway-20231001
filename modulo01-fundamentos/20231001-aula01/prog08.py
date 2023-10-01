# Laço de condição if...elif...else

"""
O laço if...elif...else faz parte das bases de qualquer linguagem de programação. Com ele possamos verificar valores e condições que
façam parte de qualquer algoritmo. Por isso o seu entendimento é fundamental.

"""

# Quando criamos variáveis com todas as letras em maiúsculo dentro do Python, indicamos que essas variáveis devem ser tratadas
# como constantes, ou seja, variáveis que não mudam de valor no decorrer do programa.
# Como o Python não possui uma palavra reservada para garantir que o valor não seja alterado (const no C#, por exemplo), isso faz parte
# das convenções de código do Python.
VISITANTE = 1
USUARIO = 2
ADMIN = 3

if __name__ == "__main__":
    
    mensagem = """
    Bem-vindo. Informe o código do tipo de usuário para continuar

    Visitante (1) - Usuario (2) - Administrador (3)
"""

    print(mensagem)

    codigo = int(input("Informe o código: "))

    # O if, assim como o elif, recebe uma expressão de comparação como "argumento". Caso essa expressão
    # resulte no valor booleano True, o bloco de código abaixo do if será executado.
    # Caso tenhamos elifs após, essas verificações serão ignoradas
    if codigo == VISITANTE:
        print("Identificado como visitante. Acesso somente leitura")

    # Caso a comparação no if não resulte em True, o elif abaixo será testado
    elif codigo == USUARIO:
        print("Identificado como usuário. Permissões comuns no sistema")
    
    elif codigo == ADMIN:
        print("Identificado como administrador. Permissão total de acesso")

    # Caso nenhuma das comparações anteriores resulte em um valor booleano True, o bloco de código
    # do else será executado. Funciona como a ação padrão caso nenhuma das outras ações sejam executadas.
    else:
        print("Código de usuário desconhecido. Sem permissões")