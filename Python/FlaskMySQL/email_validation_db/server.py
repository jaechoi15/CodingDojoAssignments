from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'emails')
app.secret_key = "secret"
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    print "hit index route"
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print "hit process route"
    errors = False
    email = request.form['email']
    print "Email entered =", email

    if len(email) < 1:
        flash("Email address is required", "error")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "error")
        errors = True
    
    if not errors:
        query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email, now(), now())"
        db = {
            "email": email
        }
        mysql.query_db(query,db)
        flash("The email address you entered {} is a valid email address! Thank you!".format(email), "success")
        return redirect("/success")
    return redirect('/')

@app.route('/success')
def success():
    print "hit success route"
    query = "SELECT id, email_address, DATE_FORMAT(created_at, '%m/%d/%Y %I:%i %p') AS created_at FROM emails ORDER BY created_at DESC"
    emails = mysql.query_db(query)
    return render_template("success.html", all_emails=emails)

@app.route('/delete/<email_id>')
def delete(email_id):
    print "hit delete route"
    print "ID =", email_id
    query = "DELETE FROM emails WHERE id = :email_id"
    db = {
        "email_id":email_id
    }
    mysql.query_db(query,db)
    return redirect('/success')

app.run(debug=True)