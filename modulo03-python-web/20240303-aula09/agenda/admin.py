from django.contrib import admin

from agenda.models import Servico, Agenda, StatusAgendamento

admin.site.register(Agenda)
admin.site.register(Servico)
admin.site.register(StatusAgendamento)
