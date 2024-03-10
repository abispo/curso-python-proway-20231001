from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Agenda, StatusAgendamento

@receiver(post_save, sender=Agenda)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StatusAgendamento.objects.create(
            agenda=instance, status=StatusAgendamento.A_CONFIRMAR
        )
