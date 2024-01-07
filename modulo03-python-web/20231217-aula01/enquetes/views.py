from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Opcao, Pergunta

def index(request):
    todas_as_perguntas = Pergunta.objects.order_by("-data_publicacao")

    contexto = {"todas_as_perguntas": todas_as_perguntas}

    return render(request, "enquetes/index.html", contexto)


def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(request, "enquetes/detalhes.html", {"pergunta": pergunta})


def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/resultados.html",
        {
            "pergunta": pergunta
        }
    )


def votar(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    try:
        opcao_escolhida = pergunta.opcao_set.get(pk=request.POST["opcao"])

    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "mensagem_erro": "Você deve escolher uma opção!"
            }
        )

    else:
        opcao_escolhida.votos += 1
        opcao_escolhida.save()

        return HttpResponseRedirect(
            reverse("enquetes:resultados", args=(pergunta.id,))
        )
