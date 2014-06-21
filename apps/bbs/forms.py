# -*- coding: utf-8 -*-
from django import forms


class ThreadCreateForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, required=True)


class TagCreateForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=1, required=True)
    thread_id = forms.IntegerField(initial=1, required=True)
