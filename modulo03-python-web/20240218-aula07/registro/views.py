from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.utils import timezone

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email
from registro.validators import (
    senha_valida,
    todos_os_dados_estao_preenchidos,
    username_ou_email_ja_cadastrado,
)

def pre_registro(request):

    if request.method == "GET":
        form = PreRegistroForm()

        return render(request, "registro/pre_registro.html", {"form": form})


    elif request.method == "POST":
        form = PreRegistroForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")

            # Pesquisa se o e-mail já não está cadastrado
            email_ja_cadastrado = User.objects.filter(email=email)

            # Verifica se o e-mail já não está no pré-registro
            email_no_pre_registro = PreRegistro.objects.filter(email=email, valido=True)

            if email_ja_cadastrado or email_no_pre_registro:
                form.add_error(
                    None,
                    "O e-mail informado não é válido! Verifique se já não possui cadastro ou ainda não confirmou o pré-registro"
                )

                return render(request, "registro/pre_registro.html", {"form": form})
            
            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            enviar_email(request, pre_registro)

            return redirect("registro:envio_email_pre_registro")


def envio_email_pre_registro(request):
    return render(request, "registro/envio_email_pre_registro.html")


def registro(request: HttpRequest):
    
    if request.method == "GET":
        
        codigo_confirmacao = request.GET.get("id")
        mensagem_erro = None
        
        pre_registro = PreRegistro.objects.filter(uuid=codigo_confirmacao).first()

        if not pre_registro or not pre_registro.valido:
            mensagem_erro = "Código de confirmação inválido. Verifique novamente."

        elif settings.TEMPO_LIMITE_PRE_REGISTRO < (timezone.now() - pre_registro.criado_em).total_seconds():
            mensagem_erro = "Código de confirmação expirado. Por favor, refaça o pré-cadastro."

        if mensagem_erro:
            return render(
                request,
                "registro/falha_confirmacao_registro.html",
                {
                    "mensagem_erro": mensagem_erro,
                    "pre_registro": pre_registro
                }
            )
        
        return render(
            request,
            "registro/registro.html",
            {
                "id_pre_registro": pre_registro.uuid,
                "email": pre_registro.email
            }
        )

    elif request.method == "POST":
        try:
            
            nome = request.POST.get("nome")
            sobrenome = request.POST.get("sobrenome")
            username = request.POST.get("username")
            senha = request.POST.get("senha")
            confirmacao_senha = request.POST.get("confirmacao_senha")
            id_pre_registro = request.POST.get("id_pre_registro")
            email = request.POST.get("email")

            mensagem_erro = None

            if not todos_os_dados_estao_preenchidos(nome, sobrenome, username, senha, confirmacao_senha, id_pre_registro, email):
                mensagem_erro = "Todos os dados são obrigatórios"

            elif username_ou_email_ja_cadastrado(username=username, email=email):
                mensagem_erro = "Existe algum problema com seu cadastro (username ou email já existem)."

            elif not senha_valida(senha=senha, confirmacao_senha=confirmacao_senha):
                mensagem_erro = "Senha e confirmação de senha são diferentes"

            if mensagem_erro:
                return render(
                    request,
                    "registro/registro.html",
                    {
                        "mensagem_erro": mensagem_erro,
                        "id_pre_registro": id_pre_registro,
                        "email": email
                    }
                )
            
            User.objects.create_user(
                username=username,
                email=email,
                password=senha,
                first_name=nome,
                last_name=sobrenome
            )

            pre_registro = PreRegistro.objects.get(uuid=id_pre_registro)
            pre_registro.valido = False
            pre_registro.save()

            return redirect("registro:sucesso_registro")

        except:
            pass


def reenviar_pre_registro(request: HttpRequest, uuid: str):
    
    if request.method == "GET":
        pre_registro = PreRegistro.objects.get(uuid=uuid)
        pre_registro.valido = False
        pre_registro.save()

        pre_registro = PreRegistro(email=pre_registro.email)
        pre_registro.save()

        enviar_email(request, pre_registro)
        
        return render(request, "registro/envio_email_pre_registro.html")
    

def sucesso_registro(request: HttpRequest):
    return render(request, "registro/sucesso_registro.html")