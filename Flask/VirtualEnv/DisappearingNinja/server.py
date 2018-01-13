from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja/<color>")
def ninja(color):
    ninjas = {
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello',
        'orange':'michelangelo'
    }

    if color in ninjas:
        character = ninjas[color]
    else:
        character = 'notapril'
    return render_template("ninja.html", character=character)


app.run(debug=True)