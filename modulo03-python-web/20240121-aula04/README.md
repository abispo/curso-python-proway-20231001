# Criar uma interface para visualização dos dados que foram salvos

Após a criação dos comandos `baixar_dados` e `carregar_dados`, será necessário criar uma interface para visualização dos resultados dos jogos do campeonato brasileiro.
Dentro do pacote `dados`, serão criadas as views, templates, urls e todos os recursos necessários para a criação das páginas para visualização. O padrão será o seguinte:
* Criação da rota `/dados` que irá listar os anos que possuem dados salvos no banco de dados.
* Cada ano será um link para a página de detalhamento do ano. Nesse detalhamento, será mostrada a lista de rodadas desse ano em específico.
* Cada item dessa lista de rodadas, será um link para a página de detalhamento da rodada, onde será mostrada a lista de jogos com suas respectivas informações: Resultado, data e hora da partida e estádio onde a partida foi realizada.

Fonte dos dados: https://github.com/abispo/Brasileirao_Dataset/