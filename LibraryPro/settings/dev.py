# LibraryPro/settings/dev.py
from .base import *
import os
from pathlib import Path

DEBUG = True

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
