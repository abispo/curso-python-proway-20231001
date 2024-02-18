from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from registro.forms import PreRegistroForm
from registro.models import PreRegistro
from registro.utils import enviar_email

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