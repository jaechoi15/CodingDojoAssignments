from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "ASDASDADA"
mysql = MySQLConnector(app, "email_address")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def process():
    email_address = request.form['email_address']
    valid = True

    if email_address == "":
        flash("Email Address field cannot be blank. Please enter an email address in the field below.")
        valid = False
    elif not EMAIL_REGEX.match(email_address):
        flash("The email address entered is not in a valid format. Please enter an email address in the following format: email@email.com")
        valid = False

    if valid == True:
        query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, now(), now())"
        data = {
            'email_address': email_address
        }
        mysql.query_db(query, data)
        flash("The email address you entered (" + (email_address) + ") is a VALID email address! Thank you!")
        return redirect('/success')
    elif valid == False:
        return redirect("/")

@app.route("/success")
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template("success.html", all_emails=emails)

@app.route("/delete/<email_id>", methods=['POST'])
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {
        'id':email_id
    }
    mysql.query_db(query, data)
    flash("The selected email")
    return 

app.run(debug=True)