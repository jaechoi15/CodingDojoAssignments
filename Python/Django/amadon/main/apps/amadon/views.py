# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return redirect('/amadon')

def main(request):
    return render(request, "amadon/index.html")

def process(request):
    request.session['quantity'] = int(request.POST['quantity'])
    print "Quantity=", request.session['quantity']

    try:
        request.session['purchase']
    except KeyError:
        request.session['purchase'] = 0
    
    try:
        request.session['price']
    except KeyError:
        request.session['price'] = 0

    try:
        request.session['items_ordered']
    except KeyError:
        request.session['items_ordered'] = 0
    
    try:
        request.session['total_purchases']
    except KeyError:
        request.session['total_purchases'] = 0
    
    if request.POST['product_id'] == 100:
        request.session['price'] = 99.99
    elif request.POST['product_id'] == 101:
        request.session['price'] = 29.99
    elif request.POST['product_id'] == 102:
        request.session['price'] = 9.99

    request.session['purchase'] = request.session['price'] * request.session['quantity']
    print "Purchase=", request.session['purchase']
    
    request.session['items_ordered'] += request.session['quantity']
    print "Items ordered=", request.session['items_ordered']

    request.session['total_purchases'] += request.session['purchase']
    print "Total purchases=", request.session['total_purchases']
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, "amadon/checkout.html")

def clear(request):
    del request.session['quantity']
    del request.session['purchase']
    del request.session['items_ordered']
    del request.session['total_purchases']
    return redirect('/')
