"""
Funções

Função pode ser entendida como um bloco de código que pode ser chamado em qualquer lugar da nossa aplicação. O paradigma procedural se baseia na criação e uso de funções.

Utilizamos a palavra reservada def para criar funções em Python

"""

def ola():
    print("Olá Mundo!")


# A função ola_nome recebe o parâmetro nome, que ficará acessível dentro dessa função
def ola_nome(nome):
    print(f"Olá {nome}")


# A função verifica a idade do usuário
def verifica_idade(nome, idade):
    if idade < 18:
        print(f"{nome}, você é menor de idade.")

    else:
        print(f"{nome}, você é maior de idade.")


# Criando funções com argumentos com valor padrão
def calculo_salario(nome, funcao, setor=1):

    salario = 0

    match setor:
        case 1:
            salario = 1000

        case 2:
            salario = 3000

        case 3:
            salario = 5000

        case _:
            pass

    mensagem = f"{nome}, sua função como {funcao} no setor {setor}, recebe R${salario}"

    print(mensagem)


# Criando uma função que retorna um valor
def calculo_imc(peso, altura):
    imc = peso / (altura * altura)

    # A palavra reservada return é utilizada para retornar um valor dentro de uma função
    return imc

if __name__ == "__main__":
    
    # Chamando a função ola()
    ola()

    # Passando um valor para o parâmetro nome
    ola_nome("Maria")

    verifica_idade("Maria", 22)

    # Somos obrigados a passar todos os valores para a função, caso não exista um valor padrão definido. Caso não passemos, recebemos um TypeError
    
    try:
        verifica_idade("João")

    except TypeError as exc:
        print(f"Erro ao chamar a função verifica_idade: {exc}")


    # Informamos apenas valores para os 2 primeiros parâmetros
    calculo_salario("Mario", "Motorista")

    # Informamos valores para todos os parâmetros
    calculo_salario("Isabel", "Advogada", setor=3)

    print(calculo_salario("Mário", "Programador", 2))

    peso = 78.5
    altura = 1.66

    mensagem = f"Maria, seu peso é {peso}kg e sua altura é {altura}m. Seu imc é de {calculo_imc(peso, altura):.1f}."

    print(mensagem)

    # Da maneira abaixo, dizemos que estamos passando os valores para os parâmetros por posição, ou seja, levamos em conta a posição definida dos parâmetros para passar os valores
    print(calculo_imc(80, 1.80))

    # Podemos passar os valores para os parâmetros em qualquer ordem, desde que indiquemos qual parâmetro está recebendo o valor.
    # Chamamos de passagem por posição ou passagem por keyword
    print(calculo_imc(altura=1.90, peso=99))