from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "session_words/index.html")

def process(request):
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    request.session['font_size'] = request.POST['font_size']
    return redirect("/show")

def show(request):
    return redirect("/")