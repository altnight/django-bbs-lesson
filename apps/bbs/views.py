# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.utils import template_response, get_user
from core.errors import ServerException

from .forms import ThreadCreateForm, TagCreateForm, CommentAddForm
from .models import Thread, Tag, Comment


@template_response('bbs/threads.html')
def threads(request):
    thread_list = Thread.objects.be().order_by('-created_at')
    return {
        'thread_list': thread_list,
    }


@template_response('bbs/thread.html')
def thread(request, id):
    """
    thread detail view
    """
    user = get_user(request)
    import debug
    try:
        thread = Thread.objects.be().get(id=id)
    except Thread.DoesNotExist:
        raise ServerException("thread not found")

    if request.method == "POST" and user:
        form = CommentAddForm(request.POST)
        if form.is_valid():
            Comment.objects.create_comment(user, thread, form.cleaned_data['body'])
            return HttpResponseRedirect(reverse("bbs:thread", args=(id, )))

    # GET
    form = CommentAddForm(request.GET)

    return {
        'thread': thread,
        'form': form,
    }


@template_response('bbs/create_thread_form.html')
def create_thread(request):
    if request.method == "POST":
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            Thread.objects.create_thread(name=form.cleaned_data['name'])
            return HttpResponseRedirect(reverse('bbs:threads'))

    form = ThreadCreateForm()
    return {'form': form}


@template_response('bbs/tag.html')
def tag(request, id):
    try:
        tag = Tag.objects.be().get(id=id)
    except Tag.DoesNotExist:
        # TODO:
        raise

    thread_list = tag.thread.be().order_by('-created_at')
    return {
        'tag': tag,
        'thread_list': thread_list,
    }


@template_response('bbs/create_tag_form.html')
def create_tag(request):
    if request.method == "POST":
        form = TagCreateForm(request.POST)
        if form.is_valid():
            Tag.objects.create_tag(
                tag_name=form.cleaned_data['name'],
                thread_id=form.cleaned_data['thread_id'],
            )
            return HttpResponseRedirect(reverse('bbs:threads'))

    form = TagCreateForm()
    thread_list = Thread.objects.be().order_by('-created_at')
    return {
        'form': form,
        'thread_list': thread_list,
    }
