from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninjas.html")

@app.route('/ninja/<color>')
def show(color):
    print color
    if color == "blue":
        turtle = "leonardo"

    elif color == "red":
        turtle = "raphael"

    elif color == "purple":
        turtle = "donatello"

    elif color == "orange":
        turtle = "michelangelo"
        
    else:
        turtle = "notapril"

    return render_template("show.html", turtle=turtle )
        
app.run(debug=True)