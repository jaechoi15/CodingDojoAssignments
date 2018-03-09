# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here
def index(request):
    print "*"*100
    print "hit index"
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    print "*"*100
    print "hit new"
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    print "*"*100
    print "hit create"
    return redirect('/')

def show(request, blog_id):
    print "*"*100
    print "hit show"
    response = "placeholder to display blog {}".format(blog_id)
    return HttpResponse(response)

def edit(request, blog_id):
    print "*"*100
    print "hit edit"
    response = "placeholder to edit blog {}".format(blog_id)
    return HttpResponse(response)

def destroy(request, blog_id):
    print "*"*100
    print "hit destroy"
    # response = "placeholder to delete blog {}".format(blog_id)
    # return HttpResponse(response)
    return redirect('/')