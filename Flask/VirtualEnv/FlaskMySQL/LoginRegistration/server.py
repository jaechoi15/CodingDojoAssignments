from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "iiwejfwf"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_reg')

@app.route('/')
def index():
    if "id" in session.keys():
        return redirect('/success')
    return render_template("index.html")

# Register
@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    c_password = request.form['c_password']

    valid = True
    # First Name validation
    if first_name == "":
        flash("First Name field cannot be empty") 
        valid = False
    elif len(first_name) < 3:
        flash("First name must have at least 3 letters")
        valid = False

    # Last Name validation
    if last_name == "":
        flash("Last Name field cannot be empty")
        valid = False
    elif len(last_name) < 3:
        flash("Last name must have at least 3 letters")
        valid = False

    # Email validation
    if email == "":
        flash("Email field cannot be empty")
        valid = False
    elif not EMAIL_REGEX.match(email):
        flash("Email is not in a valid format")
        valid = False

    # Username validation
    if username == "":
        flash("Username field cannot be empty")
        valid = False
    elif len(username) < 3:
        flash("Username must have at least 3 letters")
        valid = False

    # Password validation
    if password == "":
        flash("Password field cannot be empty")
        valid = False
    elif len(password) < 8:
        flash("Password must have at least 8 characters")
        valid = False

    # Confirm Password validation
    if c_password == "":
        flash("Confirm password cannot be empty")
        valid = False
    elif c_password != password:
        flash("Password and Confirm Password must match")
        valid = False

    if valid == True:
        query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `pw_hash`, `username`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, :password, :pw_hash, :username, now(), now())"
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "pw_hash": pw_hash,
            "username": username
        }
        mysql.query_db(query, data)
        flash("Registration is complete. Please login.")
        return redirect('/')
    elif valid == False:
        return redirect('/')

# Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = "SELECT * FROM users WHERE username = :username"
    data = {
        "username": username
    }
    user = mysql.query_db(query, data)
    if len(user) == 0:
        flash("Invalid username")
        return redirect('/')
    else:
        user = user[0]
        if bcrypt.check_password_hash(user['pw_hash'], password):
            flash("Login successful!")
            session["id"] = user["id"]
            return redirect('/success')
        else:
            flash("Invalid password")
            return redirect("/")
    return "hit login route"

# Login Success
@app.route('/success')
def success():
    query = "SELECT username FROM users WHERE id = :username"
    data = {
        "username": session["id"]
    }
    logged_user = mysql.query_db(query, data)[0]
    return logged_user["username"]


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)