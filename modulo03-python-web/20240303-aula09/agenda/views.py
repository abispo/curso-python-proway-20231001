from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Agenda

def index(request):
    return render(request, "agenda/index.html")


def agendamentos(request: HttpRequest):

    agenda_usuario = Agenda.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        "agenda/agendamentos.html",
        {"agenda_usuario": agenda_usuario}
    )

def detalhe_agendamento(request: HttpRequest, agendamento_id: int):

    agendamento = Agenda.objects.get(pk=agendamento_id)

    if agendamento.usuario == request.user:
        return render(
            request,
            "agenda/detalhe_agendamento.html",
            {"agendamento": agendamento}
        )
    
    else:
        return redirect(reverse("agenda:meus_agendamentos"))