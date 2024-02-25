from django.apps import AppConfig


class RegistroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registro'

    def ready(self) -> None:
        import registro.signals