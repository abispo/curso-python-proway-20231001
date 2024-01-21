import json
import os

from datetime import datetime
from typing import Any

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandParser

from dados.models import Clube, Partida, Rodada


class Command(BaseCommand):
    help = "Carrega os dados de um arquivo e salva no banco de dados."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("ano", type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        
        ano = options.get("ano")
        caminho_arquivo = os.path.join(os.getcwd(), "downloads", f"brasileirao-{ano}.json")

        try:
            arquivo = open(caminho_arquivo, mode="r", encoding="utf-8")
            conteudo_arquivo = json.load(arquivo)
            arquivo.close()

            chaves_rodadas = conteudo_arquivo.keys()

            for chave_rodada in chaves_rodadas:
                numero_rodada = int(chave_rodada.split("\u00aa")[0])

                rodada, _ = Rodada.objects.get_or_create(
                    numero=numero_rodada, ano=int(ano)
                )

                for partida in conteudo_arquivo[chave_rodada]:
                    
                    nome_clube_mandante = partida.get("clubs").get("home").strip().title()
                    nome_clube_visitante = partida.get("clubs").get("away").strip().title()

                    clube_mandante, _ = Clube.objects.get_or_create(nome=nome_clube_mandante)
                    clube_visitante, _ = Clube.objects.get_or_create(nome=nome_clube_visitante)

                    gols_clube_mandante = int(partida.get("goals").get("home"))
                    gols_clube_visitante = int(partida.get("goals").get("away"))

                    estadio = partida.get("stadium").strip()
                    hora_partida = partida.get("hour")
                    data_partida = partida.get("date")

                    formato_data_hora = "%d/%m/%Y %H:%M"

                    if len(data_partida) == 8:
                        formato_data_hora = "%d/%m/%y %H:%M"

                    data_hora = datetime.strptime(
                        f"{data_partida} {hora_partida}",
                        formato_data_hora
                    )

                    data_hora = timezone.make_aware(
                        data_hora
                    )

                    Partida.objects.get_or_create(
                        rodada=rodada,
                        clube_mandante=clube_mandante,
                        clube_visitante=clube_visitante,
                        gols_clube_mandante=gols_clube_mandante,
                        gols_clube_visitante=gols_clube_visitante,
                        estadio=estadio,
                        data_hora=data_hora
                    )

                    self.stdout.write(f"Partida entre {clube_mandante} e {clube_visitante} salva com sucesso.")


        except FileNotFoundError:
            self.stdout.write(f"Erro ao encontrar o arquivo {caminho_arquivo}.")