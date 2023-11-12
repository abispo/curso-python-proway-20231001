/*
Cardinalidade entre tabelas

Podemos entender como cardinalidade, o nível de relacionamento entre as
tabelas em um banco de dados, ou seja, como os registros de cada tabela
aparecem nas relações.

Temos 3 níveis de relacionamento que podem aparecer entre as tabelas:

Um Para Um			-> 	1:1
Um Para Muitos		-> 	1:N
Muitos para Muitos	-> 	N:N

Exemplo: Esquema de banco de dados para armazenar dados de postagens
estilo twitter. Teremos as seguintes informações salvas:
	- Usuario que fez a postagem
    - A postagem
    - As categorias (hashtags) associadas a cada postagem
*/

/*
Vamos salvar as informações sobre usuário em 2 tabelas:
	- tb_usuarios	-> Conterá as informações da conta (username, etc)
    - tb_perfis		-> Irá conter as informações pessoais (nome, idade, etc)
*/

CREATE TABLE IF NOT EXISTS tb_usuarios(
	id		INTEGER		PRIMARY KEY		NOT NULL,
    email	VARCHAR(100)	NOT NULL,
    senha	VARCHAR(100)	NOT NULL,
    username	VARCHAR(100)	NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_perfis(
	id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(200) NOT NULL,
    data_de_nascimento DATE NOT NULL,
    
    FOREIGN KEY(id) REFERENCES tb_usuarios(id)
);

INSERT INTO tb_usuarios(id, email, senha, username) VALUES
	(1, "maria@email.com", "123456", "mariazinha"),
    (2, "joao@email.com", "123456", "joaozinho");
SELECT * FROM tb_usuarios;

INSERT INTO tb_perfis(id, nome, data_de_nascimento) VALUES
	(1, "Maria da Silva", "1987-07-12"),
    (2, "João da Silva", "1988-12-02");
SELECT * FROM tb_perfis;

/*
Nesse caso, criamos uma relação de Um Para Um (1:1) entre as tabelas
tb_usuarios e tb_perfis, pois a coluna id da tabela tb_perfis, além de ser
uma chave primária, é uma chave estrangeira que referencia a coluna id
da tabela tb_usuarios. Ou seja, assim como não podemos ter mais de 1 perfil
para um usuário, não conseguimos criar um perfil para um usuário que não
exista na tabela tb_usuarios.
*/

INSERT INTO tb_perfis(id, nome, data_de_nascimento) VALUES
	(2, "João da Silva (perfil reserva)", "1997-01-01");