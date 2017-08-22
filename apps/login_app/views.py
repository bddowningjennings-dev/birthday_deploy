# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    return render(request, 'login_app/register.html')

def process_register(request):
    try:
        request.session['user_id']
    except:
        return redirect('/register')
    results = User.objects.validate_register(request.POST)
    if len(results['errors']) > 0:
        for error in results['errors']:
            messages.error(request, error, extra_tags='register')
        return redirect('/register')
    user = User.objects.add(request.POST)
    request.session['user_id'] = user.id
    return redirect('/dashboard')