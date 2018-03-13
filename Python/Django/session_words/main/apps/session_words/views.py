# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# Create your views here.

def index(request):
    print "hit index"
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request, "session_words/index.html")

def process(request):
    print "hit process"

    if 'size' in request.POST:
        size = "2em"
    else:
        size = "1em"
    
    word = request.POST['word']
    color = request.POST['color']
    addDate = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")
    word_list = request.session['words']

    word_list.append({
        "word": word, 
        "color": color, 
        "size": size, 
        "addDate": addDate
        })
    request.session['words'] = word_list
    
    print request.session['words']
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')