# Acesso a banco de dados utilizando o ORM SQLAlchemy

SQLAlchemy é um ORM (Object Relational Mapper | Mapeador Objeto Relacional). Basicamente utilizamos para trabalhar com banco de dados utilizando orientação a objetos.

## Instalação
De preferência, quando utilizamos pacotes de terceiros, criamos um virtualenv em python para instalação dos pacotes.

### Virtualenvs em Python
As virtualenvs (ambientes virtuais) em Python são ferramentas que permitem criar e gerenciar ambientes Python isolados do sistema global. Essa separação é especialmente útil quando você está desenvolvendo diferentes projetos que podem ter dependências diferentes, versões de bibliotecas ou até mesmo versões diferentes do Python. Abaixo, estão alguns pontos-chave sobre as virtualenvs:

* Isolamento de Ambientes:
    * Uma virtualenv cria um diretório isolado que contém sua própria instalação do Python e suas próprias bibliotecas. Isso evita conflitos entre diferentes projetos que podem depender de versões diferentes de bibliotecas.

* Instalação de Dependências:
    * Dentro de um ambiente virtual, você pode instalar e gerenciar as dependências específicas do seu projeto usando o pip, sem afetar o Python global ou outros ambientes virtuais.

* Facilidade de Criação e Ativação:
    * Criar uma virtualenv é simples usando o módulo `venv` (ou `virtualenv`, um pacote externo). Uma vez criado, você ativa o ambiente virtual para começar a usá-lo. A ativação configura a linha de comando para usar o Python e o pip específicos do ambiente virtual.

* Requisitos do Projeto:
    * Muitos projetos Python incluem um arquivo chamado requirements.txt, que lista todas as dependências do projeto. Isso facilita a replicação do ambiente em outro local ou por outros desenvolvedores.

* Ambientes para Desenvolvimento e Produção:
    * Muitas equipes de desenvolvimento usam ambientes virtuais para garantir que o ambiente de desenvolvimento seja consistente com o ambiente de produção. Isso ajuda a evitar surpresas devido a diferenças nas versões das bibliotecas.

* Integração com Ferramentas de Desenvolvimento:
    * Muitas ferramentas de desenvolvimento e ambientes de integração contínua têm suporte para ambientes virtuais. Isso facilita a configuração de projetos em diferentes etapas do ciclo de vida do desenvolvimento.

* Portabilidade:
    * Como os ambientes virtuais são isolados, você pode compartilhá-los com outros desenvolvedores ou implantá-los em diferentes sistemas operacionais, mantendo a consistência das dependências do projeto.

* Desenvolvimento Experimental:
    * Ambientes virtuais são frequentemente usados para testar bibliotecas ou versões de Python antes de comprometê-las com o ambiente global ou do projeto.

* Documentação de Ambientes:
    * Ao incluir um requirements.txt em seu projeto, você fornece uma forma documentada de reproduzir o ambiente de desenvolvimento.

Ao usar virtualenvs, os desenvolvedores podem criar ambientes Python isolados, facilitando a gestão de dependências e garantindo uma reprodução consistente do ambiente de desenvolvimento em diferentes contextos.

`pip install sqlalchemy`