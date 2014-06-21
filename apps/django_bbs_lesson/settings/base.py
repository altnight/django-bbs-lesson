# -*- coding: utf-8 -*-
import os
APPS_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),  # settings dir
    os.pardir,  # project dir
    os.pardir,
))
REOPSITORY_DIR = os.path.abspath(os.path.join(
    APPS_DIR,
    os.pardir,
))

SECRET_KEY = 'bn$w41spjz-4cm0(g&8vm9$2lzt#hcdwcw)c^oayux=is6n0&6'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'core',
    'bbs',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_bbs_lesson.urls'

WSGI_APPLICATION = 'django_bbs_lesson.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(APPS_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(REOPSITORY_DIR, "statics"),
)

TEMPLATE_DIRS = (
    os.path.join(REOPSITORY_DIR, 'templates'),
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# use session
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_CONTEXT_PROCESSORS = (
    # default
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    # apps
    'users.context_processors.current_user',
)

