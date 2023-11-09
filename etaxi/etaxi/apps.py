from django.apps import AppConfig


class EtaxiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etaxi'
    
    def ready(self):
        from etaxi import signals
