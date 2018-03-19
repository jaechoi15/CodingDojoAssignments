# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.

def index(request):
    if 'id' in request.session:
        return redirect('/success')
    return render(request, "login_registration/index.html")


def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    c_password = request.POST['c_password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    errors = User.objects.basic_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')

    User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)

    user = User.objects.get(email=email)
    request.session['id'] = user.id

    messages.success(request, "Successfully registered!")
    return redirect('/success')


def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.filter(email=email)
    if len(user) > 0:
        checkPassword = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if checkPassword:
            request.session['id'] = user[0].id
            messages.success(request, "Successfully logged in!")
            return redirect('/success')
    else:
        messages.error(request, "Incorrect username or password")
        return redirect('/')


def success(request):
    user = User.objects.get(id=request.session['id'])

    context = {
        "user": user
    }
    return render(request, "login_registration/success.html", context)


def logout(request):
    request.session.clear()
    return redirect('/')