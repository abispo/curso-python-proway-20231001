from typing import List
from django.db.models import QuerySet

from agenda.models import Agenda

from datetime import date, datetime


def gerar_lista_horarios(agenda_semanal: List[object], lista_agendas: QuerySet[Agenda]):

    horarios = []

    for dia in agenda_semanal:
        for hora in range(0, 24):
            horario_atual = datetime.strptime(dia.strftime(f"%Y-%m-%d {hora:02d}:00"), "%Y-%m-%d %H:%M")
            print("Ok")
            
        
            horarios.append({
                "hora": f"{hora:02d}:00",
                "agendas": [
                    None for _ in range(7)
                ]
            })

    return horarios