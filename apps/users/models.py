# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from core.models import (
    BaseModel,
    BaseManager,
)


class UserManager(BaseManager, BaseUserManager):
    def create_user(self, name, password, **kwargs):
        """
        Creates and saves a User with the given name and password
        """
        user = self.model(
            name=name,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password, **kwargs):
        """
        Creates and saves a superuser with the given name and password
        """
        user = self.create_user(name, password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(BaseModel, AbstractBaseUser):
    """
    App User
    """
    name = models.CharField(
        max_length=200,
        help_text=u'name',
        unique=True,
    )
    age = models.IntegerField(
        default=0,
    )

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return u'%s %s' % (self.id, self.name)

    class Meta:
        db_table = u'users'
        verbose_name = u"users"
        ordering = ['-id']
