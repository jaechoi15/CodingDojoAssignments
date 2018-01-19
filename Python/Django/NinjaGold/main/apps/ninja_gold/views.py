from django.shortcuts import render, HttpResponse, redirect
import random   

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    context = {
        "gold": request.session['gold'],
        "activities": request.session['activities']
    }
    return render(request, "ninja_gold/index.html", context)

def process_money(request):
    building = request.POST['building']
    if building == 'farm':
        gold = random.randrange(10,21)
        request.session['activities'].append({'activity': "You entered a {} and earned {} gold pieces.".format(building, gold), 'class':'win'})
    
    elif building == 'cave':
        gold = random.randrange(5,11)
        request.session['activities'].append({'activity': "You entered a {} and earned {} gold pieces.".format(building, gold), 'class':'win'})

    elif building == 'house':
        gold = random.randrange(2,6)
        request.session['activities'].append({'activity': "You entered a {} and earned {} gold pieces.".format(building, gold), 'class':'win'})

    elif building == 'casino':
        gold = random.randrange(-50,51)
        request.session['activities'].append({'activity': "You entered a {} and earned {} gold pieces.".format(building, gold), 'class':'win'})
    
    request.session['gold'] += gold
    return redirect('/')