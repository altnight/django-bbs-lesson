# -*- coding: utf-8 -*-
from django_bbs_lesson.settings.base import *  # NOQA

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(APPS_DIR, 'db.sqlite3'),
    }
}

####################
# debug
####################

INSTALLED_APPS += (
    # debug toolbar
    'django.contrib.staticfiles',
    'debug_toolbar',
    # devserver
    'devserver',
)

MIDDLEWARE_CLASSES += (
    # debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # devserver
    'devserver.middleware.DevServerMiddleware',
)

STATIC_URL = '/static/'

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # 'devserver.modules.ajax.AjaxDumpModule',
    # 'devserver.modules.profile.MemoryUseModule',
    # 'devserver.modules.cache.CacheSummaryModule',
    # 'devserver.modules.profile.LineProfilerModule',
)
