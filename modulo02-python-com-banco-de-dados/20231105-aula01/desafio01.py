"""
Ler o arquivo `cursos.csv` e salvar os dados na tabela `tb_cursos`. Essa tabela deve ter a seguinte estrutura.

```
id              INT     PRIMARY KEY AUTOINCREMENT
curso           TEXT    NOT NULL
carga_horaria   INT     NOT NULL
preco           REAL    NOT NULL
```

Após os dados terem sido salvos, vamos salvar um novo arquivo chamado `estatisticas_cursos.txt`, que terá o formato a seguir:

```
Estatísticas dos cursos

Quantidade de cursos: 10
Curso com a maior carga horária: Web Development com Django (50 horas)
Curso com o maior valor: Machine Learning Fundamentals (R$ 1200.00)

```
"""

import csv
import os
import sqlite3

connection_string = os.path.join(os.getcwd(), "db.sqlite3")
conexao = sqlite3.connect(connection_string)

if __name__ == "__main__":

    cursor = conexao.cursor()
    cursor.execute("DROP TABLE IF EXISTS tb_cursos;")

    comando = """
        CREATE TABLE IF NOT EXISTS tb_cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL,
            preco REAL NOT NULL
        );
    """

    cursor.execute(comando)

    arquivo_cursos = os.path.join(os.getcwd(), "arquivos", "cursos.csv")
    
    with open(arquivo_cursos, "r", encoding="utf-8") as arquivo:

        # 1) Abrir o arquivo cursos.csv e ler o seu conteúdo
        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            comando = "INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES ('{}', {}, {})".format(
                linha.get("curso"), linha.get("carga_horaria"), linha.get("preco")
            )

            # 2) Inserir os dados lidos do arquivo na tabela tb_cursos
            cursor.execute(comando)

        conexao.commit()
    
    # 3) Criar o arquivo estatisticas.txt

    arquivo_estatisticas = os.path.join(os.getcwd(), "estatisticas_cursos.txt")

    with open(arquivo_estatisticas, "w", encoding="utf-8") as arquivo:

        saida = """Estatísticas dos cursos

Quantidade de cursos: {}
Curso com a maior carga horária: {} ({} horas)
Curso com o maior valor: {} (R$ {:.2f})
"""
        
        """
        4) Salvar no arquivo de estatísticas a quantidade de cursos cadastrados. Podemos fazer isso de 2 maneiras: Ou utilizando a função COUNT() do banco de dados, ou retornando todos os registros e calculando a quantidade utilizando a função built-in do Python len()
        """

        # Utilizando a função de agregação COUNT()
        # comando = "SELECT COUNT(*) FROM tb_cursos"
        # resultado = cursor.execute(comando)
        # quantidade = resultado.fetchone()[0]

        # Pegando todos os registros e calculando a quantidade utilizando len()
        comando = "SELECT * FROM tb_cursos"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        quantidade = len(resultado)

        """
        5) Salvar no arquivo de estatísticas o curso com a maior carga horária. Para isso, vamos utilizar o comando de ordenação ORDER BY no SQL.
        """

        comando = "SELECT * FROM tb_cursos ORDER BY carga_horaria DESC;"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        curso_com_maior_carga_horaria = resultado[0][1]
        carga_horaria = resultado[0][2]

        """
        6) Salvar no arquivo de estatísticas o curso com o maior valor. Para isso, vamos utilizar o comando de ordenação ORDER BY no SQL.

        Nesse caso, não faremos uma nova consulta à tabela tb_cursos. Reutilizaremos o valor da variável resultado para pegar o curso mais caro.

        A função sorted irá ordenar os itens pelo preco do curso (último item da tupla). Como é um valor numérico, por padrão será ordenado do menor para o maior. Utilizando o argumento reverse, invertemos essa ordem. Por fim, pegamos o primeiro valor do resultado que é o curso mais caro
        """
        curso_mais_caro = sorted(
            resultado, key=lambda curso: curso[3], reverse=True
        )[0]
        
        arquivo.write(saida.format(
            quantidade,
            curso_com_maior_carga_horaria,
            carga_horaria,
            curso_mais_caro[1],
            curso_mais_caro[3]
        ))