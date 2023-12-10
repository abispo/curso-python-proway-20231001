# Desafio

Baixar informações sobre pokémons da PokéAPI. Você vai precisar baixar 2 tipos de informação sobre um pokémon:
* Nome do pokémon
* A que tipos esse pokémon pertence.

Para isso, teremos 2 tabelas: Tabela de pokémons, e tabela de tipos de pokémons. Para baixar os dados, vamos utilizar a biblioteca requests. O seu uso é muito simples, como no exemplo abaixo:

```python

import requests

resposta = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")

pokémon_info = resposta.json()      # Retorna a estrutura de JSON como um dicionário Python

```

Basicacamente, teremos 2 tabelas:
* `tb_pokemons`
* `tb_tipos_pokemons`

Utilize todo o conhecimento que adquirimos nas últimas aulas (SQLAlchemy, alembic, etc) para construir as classes e os seus relacionamentos. Você é livre para salvar as informações necessárias e outras que julgar necessário.