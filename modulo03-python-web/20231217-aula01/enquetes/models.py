from django.db import models

class Pergunta(models.Model):
    
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("Data de publicação")

    class Meta:
        db_table = "tb_perguntas"

    def __str__(self):
        return self.texto_pergunta
    


class Opcao(models.Model):

    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    class Meta:
        db_table = "tb_opcoes"

    def __str__(self) -> str:
        return self.texto_opcao
