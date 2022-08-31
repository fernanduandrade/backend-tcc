from django.apps import AppConfig
import os
from django.conf import settings


class TranslatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    path = os.path.join(settings.BASE_DIR, 'core')