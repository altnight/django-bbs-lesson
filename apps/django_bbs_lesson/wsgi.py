"""
WSGI config for django_bbs_lesson project.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_bbs_lesson.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
