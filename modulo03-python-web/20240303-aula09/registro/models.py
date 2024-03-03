from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

class PreRegistro(models.Model):

    email = models.EmailField("E-mail", max_length=300)
    uuid = models.UUIDField(default=uuid4)
    criado_em = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_pre_registro"


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    tipo_logradouro = models.CharField(max_length=50, null=True, blank=True)
    logradouro = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        db_table = "tb_perfis"