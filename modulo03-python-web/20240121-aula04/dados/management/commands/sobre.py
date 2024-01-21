from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = "Informações sobre o Projeto"

    def handle(self, *args, **kwargs):
        output = f"""
Dados do Brasileirão de 2003-2023
Proway \u00A9

{timezone.now().strftime('%d/%m/%Y %H:%M:%S')}
"""
        
        self.stdout.write(output)
