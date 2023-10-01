# Variáveis e tipos de dados
# Tipos booleanos (True e False)

if __name__ == "__main__":
    
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))

    # Se a idade for menor do que 21, mostra a mensagem abaixo
    if idade < 21:
        print("Você ainda é menor de idade!")

    # Se não, mostra outra mensagem
    else:
        print("Você já é maior de idade.")