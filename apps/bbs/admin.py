# -*- coding: utf-8 -*-
from django.contrib import admin

from bbs.models import Thread, Comment, Tag


admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Tag)
