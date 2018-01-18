from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

def index(request):
    return render(request, 'random_word/index.html')
