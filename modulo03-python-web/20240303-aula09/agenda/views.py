from django.http import HttpRequest
from django.shortcuts import render

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