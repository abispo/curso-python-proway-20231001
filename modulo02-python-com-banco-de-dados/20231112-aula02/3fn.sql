/*
	Terceira Forma Normal (3FN)
    
    Uma tabela está na Terceira Forma Normal (3FN), se:
    * Ela está na Segunda Forma Normal(2FN)
    * Todos os campos não chave da tabela dependem exclusivamente da
    chave primária.
*/

-- Definindo o banco de dados ativo
USE curso_python_proway_20231001_modulo02;

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id 		INTEGER		NOT NULL,
    item_id			INTEGER		NOT NULL,
    valor_unitario	FLOAT		NOT NULL,
    quantidade		INTEGER		NOT NULL,
    subtotal		FLOAT		NOT NULL
);

INSERT INTO tb_pedidos_itens(
	pedido_id, item_id, valor_unitario, quantidade, subtotal
) VALUES
	(1, 1, 10, 2, 10 * 2),
    (1, 2, 3.50, 5, 3.50 * 5),
    (2, 3, 69.90, 2, 69.90 * 2);
SELECT * FROM tb_pedidos_itens;

/*
O valor da coluna subtotal é calculado multiplicando os valores das colunas
valor_unitario e quantidade. Ou seja, a coluna subtotal depende de outras
colunas que não são chave primária da tabela. Com isso, estamos violando
uma das regras da Terceira Forma Normal (3FN).
*/

-- Apagamos a coluna subtotal
ALTER TABLE tb_pedidos_itens DROP COLUMN subtotal;

-- Calculamos o subtotal no próprio SELECT
SELECT *, valor_unitario * quantidade AS "Subtotal" FROM tb_pedidos_itens;

-- Alternativamente, podemos criar uma View com essa consulta
CREATE VIEW vw_total_pedidos AS
SELECT *, valor_unitario * quantidade AS "Subtotal"
FROM tb_pedidos_itens;

SELECT * FROM vw_total_pedidos;