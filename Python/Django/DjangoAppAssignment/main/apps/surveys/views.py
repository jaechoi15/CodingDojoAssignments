from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

def create(request):
    return redirect("/surveys")

def show(request, survey_id):
    response = "placeholder to display blog " + survey_id
    return HttpResponse(response)

def edit(request, survey_id):
    response = "placeholder to edit blog " + survey_id
    return HttpResponse(response)

def delete(request, survey_id):
    return redirect("/blogs")
