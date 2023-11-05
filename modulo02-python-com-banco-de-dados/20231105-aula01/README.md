# Python com Banco de Dados

## Trabalhando com a Biblioteca sqlite3

### Desafio 1

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

### Desafio 2

Ler o arquivo `notas.csv` e salvar as informações na tabela `tb_notas`. Essa tabela terá a seguinte estrutura:

```
id          INTEGER     PRIMARY KEY     AUTOINCREMENT
nome        TEXT        NOT NULL
nota1       REAL        NOT NULL
nota2       REAL        NOT NULL
nota3       REAL        NOT NULL
nota4       REAL        NOT NULL
nota5       REAL        NOT NULL
```

Após os dados terem sido salvos, vamos criar uma tabela com estatísticas, chamada `tb_estatisticas_notas`. A tabela terá a seguinte estrutura:

```
quantidade_de_alunos        INT     NOT NULL
media_geral                 REAL    NOT NULL
maior_media                 REAL    NOT NULL
aluno_maior_media           TEXT    NOT NULL
```

Importante: A média de cada aluno será calculada excluindo a maior e a menor notas. Exemplo:

nome;n1;n2;n3;n4;n5
Maria;4;9;10;2;5  

Nesse caso, a média da aluna Maria será calculada utilizando as 3 notas intermediárias, ou seja, [4, 5, 9]. A menor nota (2) e maior nota (10) são excluídas do cálculo, ou seja, a média de Maria será de 6.
