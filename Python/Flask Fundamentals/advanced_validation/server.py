from flask import Flask, render_template, session, flash, redirect, request
import re

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$') 
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email field cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email address is not in a valid format")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)