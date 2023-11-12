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