# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from testapi.models import SmsLog


class SmsForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя:',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=100,
        required=False,
        label='Телефон абонента:',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Ваше сообщение:',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '12'})
    )


def home(request):
    form = SmsForm()
    log = SmsLog.objects.all()
    return render(request, 'site/home.html', dict(form=form, log=log))
