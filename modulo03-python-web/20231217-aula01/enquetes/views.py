from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Pergunta

def index(request):
    todas_as_perguntas = Pergunta.objects.order_by("-data_publicacao")

    contexto = {"todas_as_perguntas": todas_as_perguntas}

    return render(request, "enquetes/index.html", contexto)


def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(request, "enquetes/detalhes.html", {"pergunta": pergunta})


def resultados(request, pergunta_id):
    return HttpResponse(f"Voce está visualizando os resultados da pergunta {pergunta_id}")


def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando em uma opção da pergunta {pergunta_id}")