from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%I:%M %p", gmtime()),
        "date": strftime("%b %d, %Y", gmtime())
    }
    return render(request, 'timedisplay/index.html', context)
