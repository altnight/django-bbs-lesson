# -*- coding: utf-8 -*-
from django import forms


class ThreadCreateForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=1)


class TagCreateForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1)
    thread_id = forms.CharField(max_length=100, min_length=1)
