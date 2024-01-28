from django.urls import path

from . import views

app_name = "dados"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:ano>/", views.lista_rodadas, name="lista_rodadas"),
    # path("<int:ano>/<int:rodada_id>/", views.partidas)
]
