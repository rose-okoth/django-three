from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import users.signals
