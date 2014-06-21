# -*- coding: utf-8 -*-
from django.db import models


class BaseManager(models.Manager):
    def be(self):
        return self.filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        help_text=u'作成日時',
        auto_now=True,
        auto_now_add=False)
    updated_at = models.DateTimeField(
        help_text=u'更新日時',
        auto_now=True,
        auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True
