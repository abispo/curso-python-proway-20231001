# Sistema de Agendamento

Sistema simples de agendamento para diversos negócios (salão de beleza, barbeiro, etc)

## Regras de negócio

1. Um usuário possui um perfil, e um perfil está associado a um usuário
2. O Profissional irá cadastrar os serviços que estarão disponíveis para serem agendados
3. O Profissional pode definir os dias e os horários que estará disponível para atendimento
4. Um Usuário pode agendar um serviço com o profissional
    * O usuário irá definir a hora de início. Por padrão, cada serviço irá durar 1 hora. Porém o Usuário pode extender esse horário
    * O usuário não poderá agendar um serviço fora do horário permitido
    * Ao final, o usuário poderá avaliar o serviço e fazer um comentário
5. O Profissional poderá cancelar um agendamento
    * Após o cancelamento, o profissional poderá enviar uma mensagem ao Usuário, explicando o cancelamento
6. O Cliente também pode cancelar o próprio agendamento

### Desafio 1

Criar a página de perfil do usuário, onde será possível atualizar os dados de perfil. Siga os seguintes passos:

1. Criar a rota `/registro/<id_usuario>/perfil`, que será a rota que levará ao perfil do usuário. `<id_usuario>` será substituído pelo id do usuário que está acessando.

2. Quando o usuário clicar nesse link (na barra de navegação), será direcionado para a página de edição de perfil do usuário, onde será mostrado um formulário com todos os campos que existem na model Perfil (todos com exceção de usuario).

3. Caso já existam informações preenchidas na tabela de perfis, elas devem ser exibidas nos elementos. Ou seja, quando o template for carregado, essas informações já devem ser enviadas para ele.

4. O usuário poderá alterar qualquer informação desse formulário, porém não poderá deixar os campos vazios (dica: Utilize o atributo required nos elementos HTML).

5. Depois que o usuário clicar no botão "Salvar", os dados serão salvos na tabela `tb_perfis` e o usuário será direcionado para a mesma página, com os dados já atualizados.