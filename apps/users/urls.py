# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users.views import (
    signup,
    login,
    logout,
)

urlpatterns = patterns(
    'users.views',

    url(
        regex=r'^login/?$',
        view=login,
        name='login',
    ),
    url(
        regex=r'^signup/?$',
        view=signup,
        name='signup',
    ),
    url(
        regex=r'^logout/?$',
        view=logout,
        name='logout',
    ),
)
