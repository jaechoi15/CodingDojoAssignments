# You're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

from flask import Flask, render_template, session, request, redirect
import random, datetime

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        print "Gold:", session['gold']
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    date = datetime.datetime.now().strftime("(%Y/%m/%d %I:%M %p)")
    building = request.form['building']
    
    if building == "farm":
        earning = random.randrange(10,21)
        session['gold'] += earning
        session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in farm:", earning
        print session['activities']
    
    elif building == "cave":
        earning = random.randrange(5,11)
        session['gold'] += earning
        session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in cave:", earning
    
    elif building == "house":
        earning = random.randrange(2,6)
        session['gold'] += earning
        session['activities'].append("Searched the {} and found {} golds. - {}".format(building, earning, date))
        print "Gold found in house:", earning

    elif building == "casino":
        earning = random.randrange(-50,51)
        session['gold'] += earning
        if earning > 0:
            session['activities'].append("Entered a {} and won {} golds. - {}".format(building, earning, date))
        elif earning < 0:
            earning = abs(earning)
            session['activities'].append("Entered a {} and lost {} golds. - {}".format(building, earning, date))
        print "Gold won/lost in casino:", earning

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)