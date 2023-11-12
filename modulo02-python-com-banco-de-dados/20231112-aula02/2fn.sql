/*
	Segunda Forma Normal (2FN)
    
    A Segunda Forma Normal (2FN) exige que:
    * A tabela já esteja na Primeira Forma Normal (1FN)
    * Todas as colunas não chave da tabela devem depender exclusivamente de todas as partes
    da chave primária. Chamamos isso de Dependência Funcional Total.
*/

-- Definindo o banco de dados ativo
USE curso_python_proway_20231001_modulo02;


CREATE TABLE IF NOT EXISTS tb_controle(
	id			INTEGER			AUTO_INCREMENT,
    servico_id	INTEGER 		NOT NULL,
    servico		VARCHAR(100) 	NOT NULL,
    total_horas	INTEGER 		NOT NULL,
    valor_hora	FLOAT			NOT NULL,
    
    PRIMARY KEY(id, servico_id)
);

INSERT INTO tb_controle(servico_id, servico, total_horas, valor_hora) VALUES
	(1, "Manutenção de PC", 6, 80),
    (1, "Manutenção de PC", 10, 80),
    (2, "Desenvolvimento de Site", 150, 100),
    (3, "Configuração de Servidor", 30, 120),
    (4, "Aulas de Programação", 80, 50);

/*
Nesse caso, a tabela tb_controle não está na Segunda Forma Normal(2FN), pois as colunas
servico e valor_hora existem em função da coluna servico_id. Ou seja, as colunas dependem
apenas de parte da chave primária, e não de toda.
A coluna total_horas depende da informação do controle do serviço realizado e qual serviço
foi realizado, ou seja, ela depende de todas as partes da chave primária.
Precisamos criar uma tabela que irá armazenar apenas as informações sobre o serviço.
*/
SELECT * FROM tb_controle;

RENAME TABLE tb_controle TO tb_controle_pre_2fn;

-- Criar a tabela de serviços
CREATE TABLE IF NOT EXISTS tb_servicos(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    valor_hora FLOAT NOT NULL
);

INSERT INTO tb_servicos(nome, valor_hora) VALUES
	("Manutenção de PC", 80),
    ("Desenvolvimento de Site", 100),
    ("Configuração de Servidor", 120),
    ("Aulas de Programação", 50);
SELECT * FROM tb_servicos;

-- Criar a tabela de controle de serviços
CREATE TABLE IF NOT EXISTS tb_controle(
	id INT AUTO_INCREMENT,
    servico_id INT NOT NULL,
    total_horas INT NOT NULL,
    
    PRIMARY KEY(id, servico_id),
    FOREIGN KEY(servico_id) REFERENCES tb_servicos(id)
);

INSERT INTO tb_controle(servico_id, total_horas) VALUES
	(1, 6),
    (1, 10),
    (2, 150),
    (3, 30),
    (4, 80);
    
SELECT * FROM tb_controle;

-- Mostrar qual o valor que iremos receber por cada serviço
SELECT
	a.id, b.nome, b.valor_hora,
    a.total_horas, b.valor_hora * a.total_horas AS "Valor a receber"
FROM tb_controle a
INNER JOIN tb_servicos b
ON a.servico_id = b.id;

UPDATE tb_servicos SET valor_hora = 90 WHERE id = 1;