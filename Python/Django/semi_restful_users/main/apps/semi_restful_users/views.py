# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.

def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "semi_restful_users/index.html", context)


def new(request):
    return render(request, "semi_restful_users/new.html")


def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "semi_restful_users/edit.html", context)


def show(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "semi_restful_users/show.html", context)


def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    User.objects.create(first_name=first_name, last_name=last_name, email=email)
    return redirect('/users')


def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/users')


def update(request):
    u = User.objects.get(id=request.POST['id'])
    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']
    u.save()
    return redirect('/users/{}'.format(u.id))