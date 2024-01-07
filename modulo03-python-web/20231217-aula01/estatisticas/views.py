from django.db.models import Avg, Count
from django.shortcuts import render

from enquetes.models import Opcao, Pergunta

def index(request):

    quantidade_de_perguntas = Pergunta.objects.count()
    quantidade_de_opcoes = Opcao.objects.count()
    perguntas_ordenadas_por_votos = Pergunta.objects.annotate(
        num_votos=Count('opcao__votos')
    ).order_by('-num_votos')
    media_opcoes_por_pergunta = Pergunta.objects.annotate(
        num_opcoes=Count('opcao')
    ).aggregate(media_opcoes=Avg('num_opcoes'))

    contexto = {
        "quantidade_de_perguntas": quantidade_de_perguntas,
        "quantidade_de_opcoes": quantidade_de_opcoes,
        "perguntas_ordenadas_por_votos": perguntas_ordenadas_por_votos,
        "media_opcoes_por_pergunta": media_opcoes_por_pergunta["media_opcoes"]
    }

    return render(
        request,
        "estatisticas/index.html",
        contexto,
    )