from flask import Flask, redirect, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "asjiojasd"

@app.route("/")
def index():
    if "mystery_num" not in session:
        session["mystery_num"] = random.randrange(0,101)
        print session["mystery_num"]
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    # session["input"] = int(request.form["input"])
    if session["mystery_num"] == int(request.form["input"]):
        session["result"] = "win"
    elif session["mystery_num"] > int(request.form["input"]):
        session["result"] = "low"
    else:
        session["result"] = "high"
    return redirect("/")

@app.route("/reset")
def reset():
    session.pop("mystery_num")
    session.pop("result")
    return redirect("/")

app.run(debug=True)