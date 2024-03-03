
from django.core.mail import send_mail
from django.http.request import HttpRequest

from registro.models import PreRegistro

def enviar_email(request: HttpRequest, pre_registro: PreRegistro):
    mensagem_email = f"""
Você recebeu esse e-mail pois você ou alguém o cadastrou no sistema de agendamento. Caso queira confirmar o cadastro, clique no link a seguir. Caso não tenha sido você, apenas ignore esse e-mail.

{'https://' if request.is_secure() else 'http://'}{request.get_host()}/registro/confirmacao-pre-registro?id={pre_registro.uuid}
"""
    
    send_mail(
        "Confirmação de pré-cadastro no sistema de agendamento",
        mensagem_email,
        "admin@localhost",
        [pre_registro.email]
    )
