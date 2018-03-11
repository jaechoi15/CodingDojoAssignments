# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    print "hit process"

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

def result(request):
    print "hit result"

    return render(request, "survey_form/result.html")