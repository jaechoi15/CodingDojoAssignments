from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return redirect("/main")

def main(request):
    return render(request, "travel_buddy/index.html")

# def register(request):
    
#     return redirect("/")

def login(request):
    # print request.POST['l_username']
    request.session["l_username"] = request.POST["l_username"]
    return redirect("/travels")

def travels(request):
    return render(request, "travel_buddy/travels.html")

def add(request):
    return render(request, "travel_buddy/add.html")