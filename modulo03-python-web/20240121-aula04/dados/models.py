from django.db import models

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    escudo = models.CharField(max_length=100, default="generico.svg")

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        db_table = "tb_clubes"


class Rodada(models.Model):
    numero = models.IntegerField(null=True)
    ano = models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"Rodada {self.numero} do campeonato brasileiro de {self.ano}."
    
    class Meta:
        db_table = "tb_rodadas"


class Partida(models.Model):
    rodada = models.ForeignKey(Rodada, on_delete=models.SET_NULL, null=True)
    clube_mandante = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True, related_name="clube_mandante")
    clube_visitante = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True, related_name="clube_visitante")
    gols_clube_mandante = models.IntegerField(default=0)
    gols_clube_visitante = models.IntegerField(default=0)
    estadio = models.CharField(max_length=200, null=True, blank=True)
    data_hora = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.clube_mandante.nome} {self.gols_clube_mandante} X {self.gols_clube_visitante} {self.clube_visitante.nome}"
    
    class Meta:
        db_table = "tb_partidas"