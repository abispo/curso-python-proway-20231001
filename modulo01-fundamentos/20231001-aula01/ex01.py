# Crie um programa que peça ao usuário para digitar um número inteiro e exiba se ele é positivo, negativo ou zero.

if __name__ == "__main__":

    numero = int(input("Informe um número inteiro"))

    if numero < 0:
        print("O número é negativo.")
    
    elif numero == 0:
        print("O número é igual a 0.")

    else:
        print("O número é positivo.")