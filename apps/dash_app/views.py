# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from django.shortcuts import render

def dash(request):
  context = {
    'users': User.objects.all(),
    'jan': User.objects.filter(b_date__month=1),
    'feb': User.objects.filter(b_date__month=2),
    'mar': User.objects.filter(b_date__month=3),
    'apr': User.objects.filter(b_date__month=4),
    'may': User.objects.filter(b_date__month=5),
    'june': User.objects.filter(b_date__month=6),
    'july': User.objects.filter(b_date__month=7),
    'aug': User.objects.filter(b_date__month=8),
    'sept': User.objects.filter(b_date__month=9),
    'oct': User.objects.filter(b_date__month=10),
    'nov': User.objects.filter(b_date__month=11),
    'dec': User.objects.filter(b_date__month=12),
  }
  return render(request, 'dash_app/dash.html', context)