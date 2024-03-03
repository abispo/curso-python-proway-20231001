from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Agenda, StatusAgendamento

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
    
def cancelar_agendamento(request: HttpRequest, agendamento_id: int):

    agendamento = get_object_or_404(Agenda, pk=agendamento_id)
    
    if request.method == "GET":
        return render(
            request,
            "agenda/cancelar_agendamento.html",
            {"agendamento": agendamento}
        )
    
    if request.method == "POST":
        motivo_cancelamento = request.POST.get("motivo_cancelamento")

        status_agendamento = agendamento.statusagendamento
        status_agendamento.descricao = motivo_cancelamento
        status_agendamento.status = StatusAgendamento.CANCELADO_PELO_CLIENTE

        status_agendamento.save()

        return redirect(reverse("agenda:meus_agendamentos"))