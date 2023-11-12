/*
A normalização de dados é um processo importante na criação das tabelas em 
um banco de dados. É um processo que ajuda a evitar problemas comuns que 
ocorrem quando os dados são armazenados de maneira desorganizada. A 
normalização ajuda a melhorar a eficiência, reduzir a redundância de dados, 
melhorar a integridade dos dados e evitar problemas de inconsistência.

Para alcançar esse objetivo, dentro do processo de normalização utilizamos 
passos que chamamos de formas normais. Existem 3 principais formas normais, 
que são a Primeira Forma Normal (1FN), Segunda Forma Normal (2FN) e 
Terceira Forma Normal (3FN).
*/

/*
A 1FN(Primeira Forma Normal) define que, cada coluna em uma tabela deve 
conter apenas valores atômicos ou indivisíveis, ou seja, valores únicos
e não compostos. Essa Forma Normal ajuda a evitar a repetição de informações
em uma mesma coluna (coluna multivalorada), o que pode levar a problema de
redundância de dados, inconsistência e performance.
*/

-- Definindo o banco de dados ativo
USE curso_python_proway_20231001_modulo02;

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200) NOT NULL,
    telefone VARCHAR(100) NOT NULL
);

-- Inserir dados de clientes
INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
	(
    "João da Silva",
    "Rua XV de Novembro, 1000, Centro, Blumenau, SC",
    "4798373610"
    );
    
INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
	(
    "Neide Carvalho",
    "Praça da Liberdade, 12, Liberdade, São Paulo, SP",
    "11948590398, 11987467772"
    );
    
INSERT INTO tb_clientes(nome, endereco, telefone) VALUES
	(
    "Maria Souza",
    "Rua dos Bandeirantes, 240, Centro, Pomerode, SC",
    "47989200192"
    );
    
SELECT * FROM tb_clientes;

/* No caso da tb_clientes, 2 regras da 1FN estão sendo violadas:
 * A coluna endereço é composta, ou seja, podemos "quebrá-la" em outras
 colunas, como tipo_logradouro, numero, etc.
 * A coluna telefone contém dados multivalorados, ou seja, uma mesma coluna
 está armazenando mais de 1 tipo do mesmo dado.
*/

-- Corrigir a tabela
-- Renomear a tabela tb_clientes
RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

-- Criar a nova tabela
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    tipo_logradouro VARCHAR(50) NOT NULL,
    logradouro VARCHAR(200) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado CHAR(2) NOT NULL
);

-- Inserir os dados na nova tabela
INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado)
VALUES(
	"João da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"
);

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado)
VALUES(
	"Neide Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"
);

INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado)
VALUES(
	"Maria Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC"
);

/*
Separando o endereço por mais colunas, a pesquisa fica muito mais fácil e rápida
de ser executada. Por exemplo, pegamos todos os clientes de SC
*/
SELECT * FROM tb_clientes;

/* Como a coluna telefone pode ser multivalorada (vários telefones para 1 cliente),
nesses casos precisamos criar uma nova tabela que irá armazenar esses valores. 
Criaremos a tabela tb_telefones
*/

CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    telefone VARCHAR(30) NOT NULL,
    
    FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_telefones(cliente_id, telefone) VALUES
	(1, "4798373610"),
    (2, "11948590398"),
    (2, "11987467772"),
    (3, "47989200192");

SELECT * FROM tb_telefones;

/*
A linha abaixo não será inserida, pois não temos um cliente com id
100. A chave estrangeira na tabela tb_telefones garante que só 
podemos inserir dados de telefone de clientes que estejam cadastrados
na tabela tb_clientes
*/
INSERT INTO tb_telefones(cliente_id, telefone) VALUES
	(100, "4190292873");
    
-- Criar cliente que não possui telefone
INSERT INTO tb_clientes(
	nome, tipo_logradouro, logradouro, numero, bairro, cidade, estado
) VALUES (
	"Robert Garcia",
    "Alameda",
    "dos Santos",
    "1000",
    "Alphaville",
    "Barueri",
    "SP"
);

/*
A consulta abaixo retorna os dados que existem em ambas as tabelas
(tb_clientes e tb_telefones). Caso exista um cliente que não possua
um telefone cadastrado, ele não será exibido nos resultados da
consulta.
*/

SELECT a.nome, b.telefone FROM tb_clientes a
INNER JOIN tb_telefones b
ON a.id = b.cliente_id;