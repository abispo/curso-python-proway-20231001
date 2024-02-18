from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path("pre-registro/", views.pre_registro, name="pre_registro"),
    path("envio-email-pre-registro/", views.envio_email_pre_registro, name="envio_email_pre_registro"),
    path("confirmacao-pre-registro/", views.registro, name="registro"),
    path("reenviar-pre-registro/<uuid>/", views.reenviar_pre_registro, name="reenviar_pre_registro")
]