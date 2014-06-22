# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.utils import template_response
from users.models import Users
from . import form


@template_response('users/signup.html')
def signup(request):
    if request.method == "POST":
        f = form.SignupForm(request.POST)
        if f.is_valid():
            user = Users.objects.create_user(
                    name=f.cleaned_data['name'],
                    password=f.cleaned_data['password'],
                    age=f.cleaned_data['age'],
                   )
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
                u = Users.objects.get(name=d['name'])
            except Users.DoesNotExist:
                return HttpResponseRedirect(reverse('users:login'))
            if not u.check_password(d['password']):
                return HttpResponseRedirect(reverse('users:login'))
            request.session['user'] = u
            return HttpResponseRedirect(reverse('core:index'))
        else:
            return HttpResponseRedirect(reverse('users:login'))
    f = form.LoginForm()
    return {'form': f}


def logout(request):
    if request.session.get('user', None):
        del request.session['user']
    return HttpResponseRedirect(reverse('core:index'))
