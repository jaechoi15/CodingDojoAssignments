from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'login_registration')
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    print "hit index route"
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    print "hit register route"

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    c_password = request.form['c_password']

    errors = False

    if len(first_name) < 1:
        flash("First name is required", "errors")
        errors = True
    
    if len(last_name) < 1:
        flash("Last name is required", "errors" )
        errors = True

    if len(email) < 1:
        flash("Email address is required", "errors")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "errors")
        errors = True

    if len(password) < 1:
        flash("Password is required", "errors")
        errors = True
    elif len(password) < 8:
        flash("Password must be more than 8 characters", "errors")
        errors = True
    
    if not password == c_password:
        flash("Password and confirmation password must match", "errors")
        errors = True

    if not errors:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": pw_hash
        }
        mysql.query_db(query, data)

        flash("Registration is successful!", "success")
    
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print "hit login route"

    email = request.form['email']
    password = request.form['password']
    errors = False

    if len(email) < 1:
        flash("Email address is required", "errors")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "errors")
        errors = True

    if len(password) < 1:
        flash("Password is required", "errors")
        errors = True

    if not errors:
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {
            "email": email
        }
        user = mysql.query_db(query, data)
        print user

        if bcrypt.check_password_hash(user[0]['password'], password):
            flash("Login successful!", "success")
            return redirect('/success')
        else:
            flash("Invalid email address or password", "errors")

    return redirect('/')

@app.route('/success')
def success():
    print "hit success route"
    return render_template("success.html")

app.run(debug=True)