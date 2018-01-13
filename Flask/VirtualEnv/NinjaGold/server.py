from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "hqoeieiojrwoirje"

@app.route("/")
def index():
    if "my_gold" not in session:
        session["my_gold"] = 0
        session["activities"] = []
    return render_template("index.html", gold=session["my_gold"], acivities=session["activities"])

@app.route("/process_money", methods=["POST"])
def process_money():
    date = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

    if request.form["place"] == "farm":
        gold = random.randrange(10,20)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + "golds from the farm! (" + date + ")")

    elif request.form["place"] == "cave":
        gold = random.randrange(5,10)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + "golds from the cave! (" + date + ")")

    elif request.form["place"] == "house":
        gold = random.randrange(2,5)
        session["my_gold"] += gold
        session["activities"].append("You earned " + str(gold) + "golds from the house! (" + date + ")")

    elif request.form["place"] == "casino":
        gold = random.randrange(-50,50)
        if gold < 0:
            session["my_gold"] -= gold
            session["activities"].append("You lost " + str(gold) + "golds from the casino! (" + date + ")")
        else:
            session["my_gold"] += gold
            session["activities"].append("You won " + str(gold) + "golds from the casino! (" + date + ")")

    return redirect("/")

app.run(debug=True)