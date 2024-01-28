# Aviso: Parte da aula de hoje foi utilizada para finalizar o projeto de dados do brasileirão

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