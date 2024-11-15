from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estatesphere.accounts'

    def ready(self):
        import estatesphere.accounts.signals

