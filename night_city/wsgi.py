"""
WSGI config for night_city project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from environs import Env
from django.core.wsgi import get_wsgi_application
from django.urls import path
from whitenoise import WhiteNoise

env = Env()
env.read_env()
MEDIA_PATH = env.str("NOICE_MEDIA_FILES")
STATIC_PATH = env.str("NOICE_STATIC_FILES")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "night_city.settings")

application = get_wsgi_application()

urlpatterns = [
    path(
        "static/",
        WhiteNoise(application, root=STATIC_PATH),
    ),
    path(
        "media/",
        WhiteNoise(application, root=MEDIA_PATH),
    ),
]

application = WhiteNoise(application, root=STATIC_PATH)
application.add_files(MEDIA_PATH, prefix="media/")
