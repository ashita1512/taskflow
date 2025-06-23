from django.apps import AppConfig

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    # We import the signals here to make sure they are registered when Django starts.
    def ready(self):
        import profiles.signals
