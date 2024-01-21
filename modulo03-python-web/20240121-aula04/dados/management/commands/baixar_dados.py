import os
from typing import Any

import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "Faz o download dos arquivos de dados do campeonato brasileiro."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("ano", type=str)

    def handle(self, *args: Any, **options: Any) -> str | None:
        
        ano = options.get("ano")

        try:
            resposta = requests.get(
                settings.URL_DADOS.format(ano)
            )

            diretorio_raiz = os.getcwd()
            diretorio_downloads = os.path.join(diretorio_raiz, "downloads")
            
            if not os.path.exists(diretorio_downloads):
                os.mkdir(diretorio_downloads)

            caminho_arquivo = os.path.join(diretorio_downloads, f"brasileirao-{ano}.json")

            with open(caminho_arquivo, mode="w", encoding="utf-8") as arquivo:
                arquivo.write(resposta.text)

            self.stdout.write(f"Arquivo '{caminho_arquivo}' salvo com sucesso.")

        except Exception as exc_info:
            self.stdout.write(f"Houve um erro ao buscar o arquivo: {exc_info}.")