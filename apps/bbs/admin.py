# -*- coding: utf-8 -*-
from django.contrib import admin

from bbs.models import Thread, Tag


admin.site.register(Thread)
admin.site.register(Tag)
