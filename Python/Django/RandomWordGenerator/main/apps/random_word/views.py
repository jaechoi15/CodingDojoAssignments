from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    if 'word' not in request.session:
        request.session['word'] = ""
    return render(request, 'random_word/index.html')

def process(request):
    request.session['word'] = get_random_string(length=12)
    print request.session['word']
    request.session['attempt'] += 1
    return redirect('/')