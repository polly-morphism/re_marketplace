"""
WSGI config for re_marketplace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "re_marketplace.settings")

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
