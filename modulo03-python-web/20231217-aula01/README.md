# Python web com Django


Criando um projeto em Django
* Preferencialmente, utilizamos um virtualenv para criar o projeto
1. `pip install django`: Esse comando irá instalar o Django
2. `django-admin startproject <nome_do_projeto>`. Esse comando irá criar o projeto
    * O ponto (.) no final indica a ferramenta que o diretório raiz do projeto será criado na mesma pasta onde estamos. Caso não indiquemos esse ponto (.) no final do comando, será criada uma pasta com o nome do projeto
3. Pra rodar o projeto, digitamos `python manage.py runserver`
4. Para criar um pacote, rodamos o comando `python manage.py startapp <nome_do_app>`
5. No arquivo `urls.py` do projeto, criamos a rota para o novo pacote.
5. Criamos o arquivo `urls.py` dentro do pacote recém criado, fazendo a ligação das rotas com as funções.

## Desafio

### Criar uma página de estatísticas do site

Na página principal do pacote `enquetes`, haverá um link para a página principal do pacote `estatisticas`, onde mostraremos as seguintes estatísticas sobre as perguntas e opções:
* Quantas perguntas estão cadastradas
* Quantas opções estão cadastradas
* Uma lista de perguntas ordenada pela quantidade de votos que recebeu (mais para menos)
* A média de opções que as perguntas têm

Dica: Para as 2 últimas estatísticas, utilize o método annotate para agregar as informações (https://docs.djangoproject.com/en/5.0/topics/db/aggregation/)