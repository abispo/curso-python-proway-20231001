# Desafio

Criar uma estrutura de tabelas que irá representar o banco de dados de uma papelaria. As tabelas serão as seguintes:

* Tabela de Usuários
    * Irá armazenar os dados de usuário, como email e senha.
* Tabela de Perfis
    * Irá armazenar o perfil associado ao usuário. Terá as colunas nome, sobrenome, data de nascimento e gênero
* Tabela de produtos
    * Irá armazenar as informações sobre os produtos da papelaria. Terá as colunas id, sku, nome, descricao, preco_unitario.
* Tabela de pedidos
    * Irá armazenar os pedidos feitos pelos usuários. Terá as colunas id, usuario_id (quem fez o pedido), e data do pedido. A relação de usuario para pedido será de 1:N
* Tabela de itens_de_pedido
    * Irá armazenar os produtos que estão associados a um pedido. Terá uma relação N:N com a tabela de pedidos. Terá as seguintes colunas: id, pedido_id, produto_id, quantidade

Na pasta arquivos, existem 3 arquivos .csv: clientes.csv, pedidos.csv, produtos.csv. Os dados no banco devem ser carregados a partir desses 3 arquivos, seguindo as regras:

* O arquivo `clientes.csv`, possui os dados dos clientes. Eles devem ser dividos entre as tabelas de usuario e de perfil:
    * email e senha, serão salvos na tabela de usuarios
    * nome, sobrenome, telefone, data de nascimento e gênero, serão salvos na tabela de perfis

* O arquivo `produtos.csv` possui dos dados dos produtos, que deverão ser salvos na tabela de produtos

* O aquivo `pedidos.csv`, terá os dados de pedidos. Caso o id do pedido se repita, significa que os produtos fazem parte do mesmo pedido. Nessa parte você precisará buscar os dados necessários para preenchimento da tabela de itens de pedido:
    * Buscar o usuário pelo email
    * Buscar o produto pelo sku
    * Já ter em mãos o id do pedido antes do pedido item ser salvo

Nesse projeto deverá ser utilizado o SQLAlchemy, dando preferência à utilização das models para salvar os dados e consultá-los. Também deverá ser utilizado o SQLAlchemy para registrar o histórico do banco. Idealmente, a cada model criada, deve ser gerada uma migration e aplicada no banco de dados.