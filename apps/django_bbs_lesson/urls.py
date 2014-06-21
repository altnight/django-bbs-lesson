from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'django_bbs_lesson.apps',

    url(r'^$', include('core.urls', namespace='core', app_name='core')),
    url(r'^users/', include('users.urls', namespace='users', app_name='users')),
    url(r'^bbs/', include('bbs.urls', namespace='bbs', app_name='bbs')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

# debug toolbar
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',

        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
