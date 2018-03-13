# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.

# Display the blank form
def index(request):
    return render(request, "survey_form/index.html")

# Capture user input into sessions
def process(request):
    try:
        request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0

    print request.session['attempt']

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    request.session['attempt'] += 1
    return redirect('/result')

# Display user input
def result(request):
    return render(request, "survey_form/result.html")