from typing import Union
from django.contrib.auth.models import User
from django.db.models import Q


def todos_os_dados_estao_preenchidos(*args) -> bool:
    return all(args)


def username_ou_email_ja_cadastrado(username: str, email: str) -> Union[User, None]:
    return User.objects.filter(Q(username=username) | Q(email=email)).first()

def senha_valida(senha, confirmacao_senha):
    return senha == confirmacao_senha