# -*- coding: utf-8 -*-
from django.db import models

from core.models import (
    BaseModel, BaseManager
)


class Thread(BaseModel):
    """
    Thread
    """
    name = models.CharField(
        max_length=200,
        help_text=u'thread title',
    )

    def __unicode__(self):
        return u"%s %s" % (self.pk, self.title)

    class Meta:
        db_table = u'thread'
        verbose_name = u"thread"
        ordering = ['-id']

class TagManager(BaseManager):

    def create_tag(self, tag_name, thread_id):
        """
        create tag object and assosiate thread
        """
        tag = self.model(
            name=tag_name,
        )
        # TODO: now save tag before manytomany field value to add
        tag.save()

        try:
            thread = Thread.objects.be().get(id=thread_id)
        except Thread.DoesNotExist:
            # TODO: form clean?
            raise
        tag.thread.add(thread)

        return tag


class Tag(BaseModel):
    """
    tag
    """
    thread = models.ManyToManyField("Thread")
    name = models.CharField(
        max_length=200,
        help_text='tag name',
    )

    objects = TagManager()

    def __unicode__(self):
        return u"%s %s" % (self.pk, self.name)

    class Meta:
        db_table = u'tag'
        verbose_name = u"tag"
        ordering = ['-id']
