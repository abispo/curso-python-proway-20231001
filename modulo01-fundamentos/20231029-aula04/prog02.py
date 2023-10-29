"""
Entrada e saída de arquivos (File I/O)

Escrita de arquivos .txt no Python

"""

if __name__ == "__main__":

    continuar = True

    # Abrimos o arquivo prog02_a.txt para escrita (w = write). Caso o arquivo não exista, ele será criado automaticamente. Porém caso o arquivo já exista, ele terá todo o seu conteúdo sobrescrito pelo novo.
    arquivo = open("prog02_a.txt", "w")
    lista_linhas = []

    while continuar:

        nome = input("Informe um nome: ")
        cidade = input("Informe uma cidade: ")
        sexo = input("Informe o sexo (M ou F): ")

        conteudo = f"""Nome: {nome}
Cidade: {cidade}
Sexo: {sexo}
{'-'*100}
"""
        
        lista_linhas.append(conteudo)
        arquivo.write(conteudo)
        
        print("Registro salvo com sucesso!")

        continuar = bool(int(input("Deseja inserir outro registro (1 para SIM e 0 para NÃO)? ")))

    arquivo.close()

    # Nesse caso, abrimos o arquivo no modo a (append), e também informamos a codificação de caracteres que o arquivo terá (utf-8). É interessante para evitar salvar caracteres que não consigam ser lidos corretamente por algum editor.
    with open("prog02_b.txt", "a", encoding="utf-8") as arquivo:
        
        # O método writelines recebe uma lista de linhas, que serão salvas de uma só vez no arquivo.
        arquivo.writelines(lista_linhas)