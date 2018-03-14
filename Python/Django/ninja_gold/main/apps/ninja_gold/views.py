# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random, datetime
# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        print "Gold:", request.session['gold']
    return render(request, "ninja_gold/index.html")

def process(request):
    date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
    building = request.POST['building']
    
    if building == "farm":
        earning = random.randrange(10,21)
        request.session['gold'] += earning
        request.session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in farm:", earning
        print request.session['activities']
    
    elif building == "cave":
        earning = random.randrange(5,11)
        request.session['gold'] += earning
        request.session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in cave:", earning
    
    elif building == "house":
        earning = random.randrange(2,6)
        request.session['gold'] += earning
        request.session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in house:", earning

    elif building == "casino":
        earning = random.randrange(-50,51)
        request.session['gold'] += earning
        if earning > 0:
            request.session['activities'].append("Entered a {} and won {} golds. - {}".format(building, earning, date))
        elif earning < 0:
            earning = abs(earning)
            request.session['activities'].append("Entered a {} and lost {} golds. - {}".format(building, earning, date))
        print "Gold won/lost in casino:", earning

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')