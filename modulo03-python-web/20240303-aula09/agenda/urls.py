from django.urls import path

from . import views

app_name = "agenda"

urlpatterns = [
    path("", views.index, name="index"),
    path("meus-agendamentos/", views.agendamentos, name="meus_agendamentos")
]
