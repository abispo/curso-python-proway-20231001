from django.urls import path

from . import views

app_name = "agenda"

urlpatterns = [
    path("", views.index, name="index"),
    path("meus-agendamentos/", views.agendamentos, name="meus_agendamentos"),
    path("agendamentos/<int:agendamento_id>/", views.detalhe_agendamento, name="detalhe_agendamento"),
    path("agendamentos/<int:agendamento_id>/cancelar", views.cancelar_agendamento, name="cancelar_agendamento"),
    path("agendamentos/agenda", views.agenda, name="agenda")
]
