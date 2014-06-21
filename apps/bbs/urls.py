# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from bbs.views import (
    threads,
    create_thread,
    create_tag,
)


urlpatterns = patterns(
    'bbs.views',

    url(
        regex=r'^threads/?$',
        view=threads,
        name='threads',
    ),
    url(
        regex=r'^thread/create/?$',
        view=create_thread,
        name='create_thread',
    ),
    url(
        regex=r'^tag/create/?$',
        view=create_tag,
        name='create_tag',
    ),
)
