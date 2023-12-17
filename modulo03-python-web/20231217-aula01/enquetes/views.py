from django.http import HttpResponse
from django.shortcuts import render

from .models import Pergunta

def index(request):
    tres_ultimas_perguntas = Pergunta.objects.order_by("-data_publicacao")[:3]

    saida = ", ".join([p.texto_pergunta for p in tres_ultimas_perguntas])

    return HttpResponse(saida)


def detalhe(request, pergunta_id):
    return HttpResponse(f"Você está visualizando os detalhes da pergunta {pergunta_id}")


def resultados(request, pergunta_id):
    return HttpResponse(f"Voce está visualizando os resultados da pergunta {pergunta_id}")


def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando em uma opção da pergunta {pergunta_id}")