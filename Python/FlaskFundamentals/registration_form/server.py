from flask import Flask, render_template, session, redirect, request, flash
import re

app = Flask(__name__)
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def validate():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    errors = False

    #First Name field validation
    if len(first_name) < 1:
        flash("First Name field cannot be blank", "error")
        errors = True
    elif first_name.isalpha() == False:
        flash("First Name field cannot contain numbers", "error")
        errors = True

    #Last Name field validation
    if len(last_name) < 1:
        flash("Last Name field cannot be blank", "error")
        errors = True
    elif last_name.isalpha() == False:
        flash("Last Name field cannot contain numbers", "error")
        errors = True

    #Email field validation
    if len(email) < 1:
        flash("Email field cannot be blank", "error")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "error")
        errors = True

    #Password field validation
    if len(password) < 1:
        flash("Password field cannot be blank", "error")
        errors = True
    elif len(password) < 9:
        flash("Password must be more than 8 characters", "error")
        errors = True
        
    #Confirm Password field validation
    if len(confirm_password) < 1:
        flash("Confirm Password field cannot be blank", "error")
        errors = True
    elif not confirm_password == password:
        flash("Password and Confirmation password must match", "error")
        errors = True

    #If no errors, then notify the user the information was entered successfully
    if not errors:
        flash("Thanks for submitting your information.", "success")

    return redirect('/')

app.run(debug=True)