from django.db import models

# Model que representa a tabela auth_user
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = "tb_servicos"


class Agenda(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, null=True)
    data_hora_inicial = models.DateTimeField()
    data_hora_final = models.DateTimeField()

    class Meta:
        db_table = "tb_agendamentos"


class StatusAgendamento(models.Model):

    AGENDADO = "agendado"
    CONCLUIDO = "concluido"
    CANCELADO_PELO_CLIENTE = "cancelado_pelo_cliente"
    CANCELADO_PELO_PROFISSIONAL = "cancelado_pelo_profissional"

    POSSIVEIS_STATUS_AGENDAMENTO = {
        AGENDADO: "Agendado",
        CONCLUIDO: "Concluído",
        CANCELADO_PELO_CLIENTE: "Cancelado pelo cliente",
        CANCELADO_PELO_PROFISSIONAL: "Cancelado pelo profissional"
    }

    agenda = models.OneToOneField(Agenda, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=100, choices=POSSIVEIS_STATUS_AGENDAMENTO)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "tb_status_agendamentos"
