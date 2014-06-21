# -*- coding: utf-8 -*-
import hashlib

from django import forms
from django.forms.util import ErrorList


class LoginForm(forms.Form):
    name = forms.CharField(
        max_length=100, min_length=2)
    password = forms.CharField(
        min_length=8, max_length=100, widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        min_length=8, max_length=100, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    name = forms.CharField(
        min_length=2, max_length=100)
    age = forms.IntegerField(
        initial=0)
    password = forms.CharField(
        min_length=8, max_length=100)
    password_confirm = forms.CharField(
        min_length=8, max_length=100, widget=forms.PasswordInput)

    def clean(self):
        # TODO: validation
        data = self.cleaned_data
        data_p = self.cleaned_data.get('password', None)
        data_p2 = self.cleaned_data.get('password_confirm', None)

        if any([data_p, data_p2]) and data_p != data_p2:
            self._errors["password"] = ErrorList([u"Invalid Password"])
        return data
