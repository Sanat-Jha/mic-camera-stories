from django.apps import AppConfig


class ContentmanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contentmanagement'
    def ready(self):
        from contentmanagement.scheduler import start
        start()