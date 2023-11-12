# Exercícios Formas Normais

## Primeira Forma Normal (1FN)

### Aplique a primeira forma normal nas seguintes tabelas:

```
PS: As colunas que contém asterisco (*) são as chaves primárias das tabelas
```

#### tb_pedidos

| *pedido_id | nome_cliente  | produto                  | quantidade |
|-----------|---------------|--------------------------|------------|
| 1         | João Silva    | Camisa, Caneca           | 2, 1       |
| 2         | Jane Smith    | Adesivo, Caneca, Cantil  | 1, 3, 2    |
| 3         | Sara Correa   | Cafeteira                | 1          |

---

#### tb_funcionarios

| *funcionario_id | nome          | endereco                               | habilidades                    |
|----------------|---------------|----------------------------------------|--------------------------------|
| 1              | John Smith    | Praça da Sé, 1000, São Paulo, SP       | HTML, CSS, JavaScript, Python  |
| 2              | Jane Doe      | Rua 7 de Setembro, 1500, Blumenau, SC  | HTML, CSS, SQL                 |
| 3              | Bob Johnson   | Rua 15 de Novembro, 56, Blumenau, SC   | Python, Java                   |

---

#### tb_filmes

| nome_filme   | ano_lancamento | diretor              | ator_1            | ator_2            | ator_3            |
|--------------|----------------|----------------------|-------------------|-------------------|-------------------|
| Tubarão      | 1975           | Steven Spielberg     | Roy Scheider      | Robert Shaw       | Richard Dreyfuss  |
| Titanic      | 1997           | James Cameron        | Leonardo DiCaprio | Kate Winslet      | Billy Zane        |
| Forrest Gump | 1994           | Robert Zemeckis      | Tom Hanks         | Robin Wright      | Gary Sinise       |

---

## Segunda Forma Normal (2FN)

### Aplique a Segunda Forma Normal nas seguintes tabelas

| *Código Pedido | *Código Produto | Nome Produto | Categoria | Preço | Quantidade |
|---------------|----------------|--------------|-----------|-------|------------|
| 1001          | 001            | Camiseta     | Vestuário | 29.99 | 2          |
| 1001          | 002            | Caneca       | Casa      | 12.99 | 1          |
| 1002          | 002            | Caneca       | Casa      | 12.99 | 3          |
| 1002          | 003            | Adesivo      | Papelaria | 1.99  | 5          |

---

| *Código Pedido | Nome Cliente | Endereço Cliente      | Cidade Cliente | *Código Produto | Nome Produto | Preço |
|---------------|--------------|-----------------------|----------------|----------------|--------------|-------|
| 1001          | João Silva   | Rua das Flores, 123   | São Paulo      | 001            | Camiseta     | 29.99 |
| 1001          | João Silva   | Rua das Flores, 123   | São Paulo      | 002            | Caneca       | 12.99 |
| 1002          | Ana Santos   | Av. das Palmeiras, 45 | Rio de Janeiro | 002            | Caneca       | 12.99 |
| 1002          | Ana Santos   | Av. das Palmeiras, 45 | Rio de Janeiro | 003            | Adesivo      | 1.99  |

---

| *Código Disciplina | Nome Disciplina      | Departamento | Nome Professor | *Código Aluno   | Nome Aluno  | Nota |
|-------------------|----------------------|--------------|----------------|----------------|-------------|------|
| 1001              | Cálculo I            | Matemática   | Ana Souza      | 001            | João Silva  | 8.0  |
| 1001              | Cálculo I            | Matemática   | Ana Souza      | 002            | Ana Santos  | 6.5  |
| 1002              | Programação I        | Computação   | Pedro Silva    | 002            | Ana Santos  | 9.0  |
| 1002              | Programação I        | Computação   | Pedro Silva    | 003            | Carlos Lima | 7.5  |

---

## Terceira Forma Normal (3FN)

### Aplique a Terceira Forma Normal nas seguintes tabelas

| Disciplina       | Aluno           | Nota 1 | Nota 2 | Nota 3 | Média |
|------------------|-----------------|--------|--------|--------|-------|
| Estatística      | João Silva      | 8.5    | 9.0    | 8.5    | 8.6   |
| Matemática       | Maiara Nogueira | 10.0   | 9.5    | 9.5    | 9.6   |
| Java             | Danielle Souza  | 7.5    | 7.5    | 7.0    | 7.3   |
| Ciência de Dados | José Duarte     | 6.5    | 5.5    | 7.5    | 6.5   |

---

| *ID   | *ID Servico | Total de Horas | Valor Hora | Subtotal |
|------|------------|----------------|------------|----------|
| 0001 | 0001       | 40             | 10         | 400      |
| 0002 | 0002       | 12             | 40         | 480      |
| 0003 | 0002       | 10             | 40         | 400      |
| 0004 | 0003       | 30             | 20         | 600      |

---

# Exercícios Cardinalidade

# Exercícios

1. Crie o banco de dados biblioteca, com 2 tabelas: tb_livros e tb_detalhes_livros. Essas tabelas devem ter um relacionamento 1:1 entre elas
2. Crie o banco de dados hospital, com 2 tabelas: tb_pacientes e tb_detalhes_pacientes. Essas tabelas devem ter um relacionamento 1:1 entre elas
3.  Crie uma base de dados loja, com as tabelas tb_clientes e tb_pedidos. Cada cliente pode fazer diversos pedidos, mas cada pedido está associado a apenas 1 cliente. Defina um relacionamento 1:N entre essas tabelas.
4.  Crie uma base de dados locadora, com as tabelas tb_clientes e tb_alugueis. Cada cliente pode alugar mais de um filme, mas cada aluguel está associado a apenas 1 cliente. Defina um relacionameto 1:N.
5.  Crie um banco de dados streaming, com as tabelas tb_usuarios e tb_playlists. Cada usuário pode criar múltiplas playlists, Mas cada playlist pertence a apenas 1 usuário. Defina um relacionamento 1:N.
6.  Crie uma base de dados hotel, Com tabelas para hóspedes e reservas. Cada hóspede pode ter muitas reservas, Mas cada reserva está associada a apenas 1 cliente. Defina um relacionamento 1:N.
7. Considere o seguinte cenário: Uma universidade oferece diversos cursos, e cada curso pode ter múltiplos estudantes. Além disso, um estudante pode estar associado a diversos cursos. Faça o design das tabelas que represente essa relação N:N.
8. Uma loja vende vários produtos, e cada produto pode ser comprado por múltiplos clientes. Um cliente pode comprar vários produtos. Crie as tabelas representando essa relação N:N.