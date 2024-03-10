import calendar

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .models import Agenda, StatusAgendamento
from .utils import gerar_lista_horarios

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

def agenda(request):
    data_atual = timezone.now()
    ano_atual = data_atual.year
    mes_atual = data_atual.month

    tipo_visualizacao = request.GET.get("visualizacao", "mensal")

    calendario = calendar.Calendar(firstweekday=calendar.SUNDAY)
    agenda = calendario.monthdatescalendar(ano_atual, mes_atual)

    match tipo_visualizacao:
        case "mensal":
            return render(
                request,
                "agenda/agenda_mensal.html",
                {
                    "agenda": agenda,
                    "data_atual": data_atual
                }
            )

        case "semanal":
            
            semana_escolhida = 1
            dias_semana = []

            for indice, semana in enumerate(agenda, start=1):
                for data in semana:
                    if data_atual.date() == data:
                        semana_escolhida = indice

            for data in agenda[semana_escolhida-1]:
                dias_semana.append(data)

            return render(
                request,
                "agenda/agenda_semanal.html",
                {
                    "dias_semana": dias_semana,
                    "lista_horarios": gerar_lista_horarios()
                }
            )
