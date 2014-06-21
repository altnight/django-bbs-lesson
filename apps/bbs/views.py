# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import forms
from .models import Thread, Tag
from core.utils import template_response


@template_response('bbs/threads.html')
def threads(request):
    thread_list = Thread.objects.all()
    return {
        'thread_list': thread_list,
    }


@template_response('bbs/create_thread_form.html')
def create_thread(request):
    # TODO:
    if request.method == "POST":
        form = forms.ThreadCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Thread.objects.create(title=data['title'])
        return HttpResponseRedirect(reverse('bbs:threads'))
    else:
        form = forms.ThreadCreateForm()
        return HttpResponseRedirect(reverse('bbs:create_thread', kwargs={'form': form}))


@template_response('bbs/create_tag_form.html')
def create_tag(request):
    if request.method == "POST":
        form = forms.TagCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            t = Tag.objects.create(name=data['name'])
            th = Thread.objects.get(id=data['thread_id'])
            t.thread.add(th)
            return HttpResponseRedirect(reverse('bbs:threads'))
        else:
            return {
                'form': form,
            }
    else:
        form = forms.TagCreateForm()
        thread_list = Thread.objects.all()
        return {
            'form': form,
            'thread_list': thread_list,
        }
        # TODO:
        #return HttpResponseRedirect(reverse('bbs:create_tag', kwargs={'form': form}))
