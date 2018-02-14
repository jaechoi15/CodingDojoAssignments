from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    print session['counter']
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    print "add 2"
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print "reset"
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)