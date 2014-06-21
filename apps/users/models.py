# -*- coding: utf-8 -*-
from django.db import models

from core.models import BaseModel


class Users(BaseModel):
    """
    App User
    """
    # TODO: use abstract base user
    name = models.CharField(
        max_length=200,
        help_text=u'name',
        unique=True,
    )
    password = models.CharField(
        max_length=200,
        help_text=u'password',
    )
    age = models.IntegerField(
        default=0,
    )

    def __unicode__(self):
        return u'%s %s' % (self.name, self.age)

    class Meta:
        db_table = u'users'
        verbose_name = u"users"
        ordering = ['-id']
