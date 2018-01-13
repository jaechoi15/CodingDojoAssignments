from flask import Flask, render_template, session, redirect, request, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "asdasda"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    errors = False

    # Email field validation
    if len(request.form["email"]) == 0:
        flash("Email field cannot be blank", "error")
        errors = True
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address format", "error")
        errors = True

    # First Name field validation
    if len(request.form["first_name"]) == 0:
        flash("First Name field cannot be blank", "error")
        errors = True
    elif request.form["first_name"].isalpha() == False: 
        flash("First Name field cannot contain numbers", "error")
        errors = True

    # Last Name field validation
    if len(request.form["last_name"]) == 0:
        flash("Last Name field cannot be blank", "error")
        errors = True
    elif request.form["last_name"].isalpha() == False: 
        flash('Last Name field cannot contain numbers', "error")
        errors = True

    # Password field validation
    if len(request.form["password"]) == 0:
        flash("Password field cannot be blank", "error")
        errors = True
    elif len(request.form["password"]) < 8:
        flash("Password must be more than 8 characters", "error")
        errors = True
    elif request.form["password"] != request.form["confirm_password"]:
        flash("Password and Confirm Password fields must match", "error")
    
    # Confirm Password validation
    if len(request.form["confirm_password"]) == 0:
        flash("Confirm Password field cannot be blank", "error")
        errors = True

    if not errors:
        flash("Thank you for submitting your information.", "validation_success")

    return redirect("/")

app.run(debug=True)