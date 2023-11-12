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

-- As 2 instruções abaixo não serão executadas
INSERT INTO tb_perfis(id, nome, data_de_nascimento) VALUES
	(2, "João da Silva (perfil reserva)", "1997-01-01");
    
INSERT INTO tb_perfis(id, nome, data_de_nascimento) VALUES
	(20, "João da Silva (perfil reserva)", "1997-01-01");
    
/*
Vamos criar a tabela que irá armazenar as postagens realizadas pelos
usuários. A regra é a seguinte: Cada usuário pode fazer quantas postagens
quiser (nenhuma, uma ou várias). Porém cada postagem terá apenas 1 autor.
*/

CREATE TABLE IF NOT EXISTS tb_postagens(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    usuario_id INTEGER NOT NULL,
    titulo VARCHAR(200),
    corpo TEXT NOT NULL,
    
    FOREIGN KEY (usuario_id) REFERENCES tb_usuarios(id)
);
SELECT * FROM tb_usuarios;

INSERT INTO tb_postagens(usuario_id, titulo, corpo) VALUES
	(1, "Python é legal", "Python é muito legal"),
    (1, "Java é legal", "Java é legal");

SELECT * FROM tb_postagens;

/*
Nesse caso, percebemos que 1 usuário pode fazer quantas postagens quiser no
sistema. Enquanto cada postagem pode ter como autor apenas 1 usuário. Essa
situação caracteriza uma relação de 1:N da tabela tb_usuarios para a tabela
tb_postagens. Podemos também observar a quantidade de ocorrência de um id
da tabela tb_usuarios na tabela tb_postagens. Na esmagadora maioria dos
casos, a tabela que possui a coluna de chave estrangeira será o lado N
da relação Um para Muitos (1:N).
*/

/*
Deve ser possível associar categorias às postagens, de uma maneira similar
ao funcionamento das hashtags no twitter. Para isso, vamor criar a tabela
tb_categorias
*/

CREATE TABLE IF NOT EXISTS tb_categorias(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL
);

INSERT INTO tb_categorias (nome) VALUES
	("SQL"),
    ("Bancos de Dados"),
    ("Proway"),
    ("Programação"),
    ("Python");
SELECT * FROM tb_categorias;
/*
A regra entre postagens e categorias é a seguinte: Uma postagem pode ter
diversas categorias associadas a ela, e uma categoria pode aparecer em
várias postagens.

Nesse cenário, a regra a se fazer é criar uma tabela associativa entre
tb_postagens e tb_categorias. Essa tabela associativa terá as chaves
estrangeiras para postagens e categorias, assim sendo possível implementar
essa regra de negócio.
*/

-- Criar a tabela associativa entre postagens e categorias
CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
	postagem_id INT NOT NULL,
    categoria_id INT NOT NULL,
    
    PRIMARY KEY(postagem_id, categoria_id),
    FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
    FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
);

INSERT INTO tb_postagens_categorias(postagem_id, categoria_id) VALUES
	(1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4);
SELECT * FROM tb_postagens_categorias;

-- Mostrando as postagens e as categorias associadas a elas
SELECT tbp.id, tbp.titulo, tbc.nome FROM tb_postagens tbp
INNER JOIN tb_postagens_categorias tbpc
ON tbp.id = tbpc.postagem_id
INNER JOIN tb_categorias tbc
ON tbpc.categoria_id = tbc.id;

-- Mostrando em quantas postagens uma hashtag aparece
SELECT tbc.id, tbc.nome, COUNT(tbp.id) as ocorrencias FROM tb_categorias tbc
LEFT JOIN tb_postagens_categorias tbpc
ON tbc.id = tbpc.categoria_id
LEFT JOIN tb_postagens tbp
ON tbpc.postagem_id = tbp.id
GROUP BY tbc.id
ORDER BY ocorrencias DESC;