from django.shortcuts import get_object_or_404, render

from dados.models import Partida, Rodada

def index(request):

    todos_anos = Rodada.objects.values("ano").distinct()
    anos = [ano_info.get("ano") for ano_info in todos_anos]
    anos.sort()

    return render(request, "dados/index.html", {"anos": anos})


def lista_rodadas(request, ano):
    todas_rodadas = Rodada.objects.filter(ano=ano).order_by("numero")

    return render(request, "dados/lista_rodadas.html", {"ano": ano, "todas_rodadas": todas_rodadas})


def detalhe_rodada(request, ano, rodada_id):
    rodada = get_object_or_404(Rodada, pk=rodada_id, ano=ano)
    todas_partidas = Partida.objects.filter(rodada=rodada)

    return render(
        request,
        "dados/detalhe_rodada.html",
        {
            "rodada": rodada,
            "todas_partidas": todas_partidas
        }
    )
