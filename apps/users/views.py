# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.utils import template_response
from users.models import Users
from . import form


@template_response('users/signup.html')
def signup(request):
    # TODO: template signup, name, password
    if request.method == "POST":
        f = form.SignupForm(request.POST)
        if f.is_valid():
            # rename form -> forms
            # TODO: use manager
            name = f.cleaned_data['name']
            age = f.cleaned_data['age']
            # TODO:
            password = f.cleaned_data['password']
            # TODO: kwargs?
            user = Users.objects.create(name=name, age=age, password=password)
            request.session['user'] = user
            return HttpResponseRedirect(reverse('core:index'))
        else:
            return HttpResponseRedirect(reverse('users:signup'))

    f = form.SignupForm()
    return {'form': f}


@template_response('users/login.html')
def login(request):
    # TODO: template fix to login(not password_confirm)
    if request.method == "POST":
        f = form.LoginForm(request.POST)
        if f.is_valid():
            d = f.cleaned_data
            # TODO: moveform validation?
            try:
                u = Users.objects.get(name=d['name'], password=d['password'])
            except Users.DoesNotExist:
                return HttpResponseRedirect(reverse('users:login'))
            request.session['user'] = u
            return HttpResponseRedirect(reverse('core:index'))
        else:
            # TODO:
            #template_response('index.html')
            return HttpResponseRedirect(reverse('users:login'))
    f = form.LoginForm()
    return {'form': f}


def logout(request):
    if request.session.get('user', None):
        del request.session['user']
    return HttpResponseRedirect(reverse('core:index'))
