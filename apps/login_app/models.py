# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import datetime
from django.db import models

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class UserManager(models.Manager):
  def validate_register(self, postData):
    results = {
      'errors': [],
    }
    for data in postData:
      if str(data) != 'email':
        if len(postData[data]) < 3 and str(data) != 'b_date':
          results['errors'].append('{} field must at least 3 characters long'.format(' '.join(data.split('_')).capitalize()))
      elif not re.match(EMAIL_REGEX, postData['email']):
        results['errors'].append('Invalid Email')
      elif User.objects.filter(email=postData['email']).count() > 0:
          results['errors'].append('Email already registered')
    if len(postData['b_date']) < 1:
      results['errors'].append('Birthday cannot be blank')
    else:
      date_arr = map(int, postData['b_date'].split('-'))
      today = datetime.date.today()
      b_date = datetime.date(date_arr[0],date_arr[1],date_arr[2])
      age = today - b_date
      age = age.days/365.25
      if age < 18:
        results['errors'].append('Must be over 18 years old')
    return results

  def add(self, postData):
    date_arr = map(int, postData['b_date'].split('-'))
    b_date = datetime.date(date_arr[0],date_arr[1],date_arr[2])
    user = User()
    user.first_name = postData['first_name'].capitalize()
    user.last_name = postData['last_name'].capitalize()
    # user.b_date = time.strptime(postData['b_date'], "%Y-%m-%d")
    user.b_date = b_date
    user.email = postData['email']
    user.save()
    return user

  def validation_login(self, postData):
    results = {
      'errors': [],
    }
    for data in postData:
      if len(postData[data]) < 1 and str(data) != 'c_password':
        results['errors'].append('{} field may not be blank'.format(data.capitalize()))
    if User.objects.filter(email=postData['email']).count() < 1:
        results['errors'].append('Email/Password not currently registered')
    else:
      hashed_pw = User.objects.filter(email=postData['email'])[0].password
      if not bcrypt.checkpw(postData['password'].encode(), hashed_pw.encode()):
        results['errors'].append('Email/Password not valid')        
    return results

class User(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  b_date = models.DateField()
  email = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  objects = UserManager()
  def __str__(self):
    return '\nUser:\nfirst_name: {}\nlast_name: {}\nb_date: {}\nemail: {}\n'.format(self.first_name, self.last_name, self.b_date, self.email)
