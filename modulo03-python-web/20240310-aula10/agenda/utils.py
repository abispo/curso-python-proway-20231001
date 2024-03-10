from django.db.models import QuerySet

from agenda.models import Agenda

from datetime import date


def gerar_lista_horarios(lista_agendas: QuerySet[Agenda]):

    horarios = []

    for hora in range(0, 24):

        for agenda in lista_agendas:
            horario_agenda = agenda.data_hora_inicial
            horario_atual = horario_agenda.strptime(
                horario_agenda.strftime(f"%Y-%m-%d {hora:02d}:00"),
                "%Y-%m-%d %H:%M"
            )
        
            horarios.append({
                "hora": f"{hora:02d}:00",
                "agendas": [
                    None for _ in range(7)
                ]
            })

    return horarios