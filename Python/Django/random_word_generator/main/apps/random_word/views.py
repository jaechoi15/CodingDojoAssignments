# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'word' not in request.session:
        request.session['word'] = get_random_string(length=14)
    
    if 'count' not in request.session:
        request.session['count'] = 0

        print "Random word = ", request.session['word']
    return render(request, 'random_word/index.html')

def process(request):
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)

    print "Random word = ", request.session['word'] 
    return redirect('/')

def reset(request):
    del request.session['word']
    del request.session['count']

    return redirect('/')