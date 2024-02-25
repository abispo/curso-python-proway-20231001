from django.db import models

# Model que representa a tabela auth_user
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)

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
    agenda = models.OneToOneField(Agenda, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)

    class Meta:
        db_table = "tb_status_agendamentos"
