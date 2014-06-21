# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from core.views import index

urlpatterns = patterns(
    'core.views',

    url(
        regex=r'^$',
        view=index,
        name='index'
    ),
)
