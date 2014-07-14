# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from core.models import (
    BaseModel, BaseManager
)
from users.models import User


class ThreadManager(BaseManager):

    def create_thread(self, name):
        """
        create thread object
        """
        thread = self.model(
            name=name,
        )
        thread.save()

        return thread


class Thread(BaseModel):
    """
    Thread
    """
    name = models.CharField(
        max_length=200,
        help_text=u'thread title',
    )

    objects = ThreadManager()

    @property
    def tags(self):
        return self.tag_set.be().order_by('-created_at')

    @property
    def comments(self):
        return self.comment_set.be().order_by('-created_at')

    def get_absolute_url(self):
        return reverse('bbs:thread', args=[str(self.id)])

    def __unicode__(self):
        return u"%s %s" % (self.pk, self.name)

    class Meta:
        db_table = u'thread'
        verbose_name = u"thread"
        ordering = ['-id']


class CommentManager(BaseManager):

    def create_comment(self, user, thread, body):
        """
        create comment object
        """
        comment = self.model(
            thread=thread,
            user=user,
            body=body,
        )
        comment.save()

        return comment


class Comment(BaseModel):
    """
    thread comment
    """
    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(User)
    body = models.CharField(
        max_length=255,
        help_text=u'message body',
    )

    objects = CommentManager()

    def __unicode__(self):
        return u"%s %s" % (self.pk, self.body)

    class Meta:
        db_table = u'comment'
        verbose_name = u"comment"
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
