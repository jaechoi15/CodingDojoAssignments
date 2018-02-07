from flask import Flask, render_template, session, redirect, request, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key="asasdad"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if len(request.form["email"]) == 0:
        flash("The Email field cannot be empty!")
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address.")
    else:
        flash("Success!")
    return redirect("/")

app.run(debug=True)