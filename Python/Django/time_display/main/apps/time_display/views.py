# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    print "*"*100
    print "hit index"
    
    context = {
        "date": strftime("%B %d, %Y"),
        "time": strftime("%I:%M %p")
    }
    return render(request, "time_display/index.html", context)