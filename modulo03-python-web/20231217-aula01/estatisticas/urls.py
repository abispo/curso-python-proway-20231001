from django.urls import path

from . import views

app_name = "estatisticas"

urlpatterns = [
    path("", views.index, name="index"),
]
