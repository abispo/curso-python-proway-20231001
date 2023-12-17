from django.urls import path

from . import views

app_name = "enquetes"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pergunta_id>/", views.detalhe, name="detalhe"),
    path("<int:pergunta_id>/resultados", views.resultados, name="resultados"),
    path("<int:pergunta_id>/votar", views.votar, name="votar")
]
