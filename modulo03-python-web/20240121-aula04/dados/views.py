from django.shortcuts import render

from dados.models import Rodada

def index(request):

    todos_anos = Rodada.objects.values("ano").distinct()
    anos = [ano_info.get("ano") for ano_info in todos_anos]
    anos.sort()

    return render(request, "dados/index.html", {"anos": anos})


def lista_rodadas(request, ano):
    todas_rodadas = Rodada.objects.filter(ano=ano).order_by("numero")

    return render(request, "dados/lista_rodadas.html", {"ano": ano, "todas_rodadas": todas_rodadas})


def partidas(request, ano, rodada_id):
    return render(request, "dados/partidas.html")