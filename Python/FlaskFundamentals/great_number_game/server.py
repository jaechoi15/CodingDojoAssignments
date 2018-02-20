#Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    if 'mystery_num' not in session:
        session['mystery_num'] = random.randrange(1, 101)
        print "New Mystery Number =", session['mystery_num']
        
    else:
        print "Existing Mystery Number =", session['mystery_num']
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    # If the user's guess matches the mystery number, then notify the user the guess is correct.
    if session['mystery_num'] == int(request.form['guess']):
        session['result'] = "correct"
        print "Guess {} is {}!".format(request.form['guess'], session['result'])

    # If the user's guess is greater than the mystery number, then notify the user the guess is too high.
    elif session['mystery_num'] < int(request.form['guess']):
        session['result'] = "too high"
        print "Guess {} is {}!".format(request.form['guess'], session['result'])

    # If the user's guess is less than the mystery number, then notify the user the guess is too low.
    else:
        session['result'] = "too low"
        print "Guess {} is {}!".format(request.form['guess'], session['result'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('mystery_num')
    session.pop('result')
    return redirect('/')

app.run(debug=True)