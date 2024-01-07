# Python web com Django


Criando um projeto em Django
    * Preferencialmente, utilizamos um virtualenv para criar o projeto
    1. pip install django: Esse comando irá instalar o Django
    2. django-admin startproject <nome_do_projeto> .
        * O ponto (.) no final indica a ferramenta que o diretório raiz do projeto será criado na mesma pasta onde estamos. Caso não indiquemos esse ponto (.) no final do comando, será criada uma pasta com o nome do projeto
    3. Pra rodar o projeto, digitamos python manage.py runserver
    4. Para criar um pacote, rodamos o comando python manage.py startapp <nome_do_app>