from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'thewall')
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$')

# root
@app.route('/')
def index():
    print "hit index route"
    if "logged_id" in session.keys():
        return redirect('/wall')
    return render_template("index.html")

# registration page
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
    
    # check_query = mysql.query_db("SELECT email FROM users WHERE email = :email")
    # check_data = {
    #     "email":email
    # }
    # check_email = mysql.query_db(check_query, check_data)

    # first name field validation
    if len(first_name) < 1:
        flash("First name is required", "errors")
        errors = True
    
    # last name field validation
    if len(last_name) < 1:
        flash("Last name is required", "errors" )
        errors = True

    # Email Address field validation
    if len(email) < 1:
        flash("Email address is required", "errors")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "errors")
        errors = True

    #  for i in (mysql.query_db(check)):
    #     if i['email'] == email:
    #         flash("Email already in database")
    #         return redirect('/')

    # Password field validation
    if len(password) < 1:
        flash("Password is required", "errors")
        errors = True
    elif len(password) <= 8:
        flash("Password must be 8 or more characters long", "errors")
        errors = True
    
    # password fields validation
    if not password == c_password:
        flash("Passwords do not match", "errors")
        errors = True

    # Successful registration
    if not errors:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": pw_hash
        }
        mysql.query_db(query, data)
        flash("Registration is complete. Please login.", "success")
    return redirect('/')

# Login
@app.route('/login', methods=['POST'])
def login():
    print "hit login route"

    email = request.form['email']
    password = request.form['password']
    errors = False

    # First Name field validation
    if len(email) < 1:
        flash("Email address is required", "errors")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Email address is not in a valid format", "errors")
        errors = True

    # Password field validation
    if len(password) < 1:
        flash("Password is required", "errors")
        errors = True

    # Successful login
    if not errors:
        query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data = {
            "email": email
        }
        user = mysql.query_db(query, data)
        print "*"*100
        print user

        if bcrypt.check_password_hash(user[0]['password'], password):
            session['logged_id'] = user[0]['id']
            print "*"*100
            print "User ID = ", session['logged_id']
            print "*"*100
            # flash("Login successful!", "success")
            return redirect('/wall')
        else:
            flash("Invalid email address or password", "errors")
    return redirect('/')

# Display the user's wall page
@app.route('/wall')
def show():
    print "hit wall route"

    query_name = "SELECT CONCAT(first_name, ' ', last_name) as full_name FROM users WHERE id = :id"
    data_name = {
        "id": session['logged_id']
    }
    fullname = mysql.query_db(query_name, data_name)[0]['full_name']
    print "*"*100
    print "User's Name = ", fullname

    # retrieve all messages
    query_messages = "SELECT messages.id, messages.message, DATE_FORMAT(messages.created_at,'%M %d, %Y %h:%i %p') AS created_at, CONCAT(users.first_name, ' ', users.last_name) as full_name FROM messages JOIN users ON messages.user_id = users.id"
    all_messages = mysql.query_db(query_messages)
    print "*"*100
    print "MESSAGES"
    print "*"*100
    print all_messages

    #retrieve all comments
    query_comments = "SELECT comments.id, comments.user_id, comments.message_id, comments.comment, DATE_FORMAT(comments.created_at,'%M %d, %Y %h:%i %p') AS created_at, messages.id, CONCAT(users.first_name, ' ', users.last_name) as full_name FROM comments JOIN messages ON comments.user_id = messages.user_id JOIN users on messages.user_id = users.id"
    all_comments = mysql.query_db(query_comments)
    print "*"*100
    print "COMMENTS"
    print "*"*100
    print all_comments
    
    user_comments = all_comments[0]['comment']

    return render_template("wall.html", fullname=fullname, all_messages=all_messages, all_comments=all_comments)

@app.route('/post_message', methods=['POST'])
def post_message():
    print "hit post_message route"

    user_id = session['logged_id']
    post_message = request.form['message']
    errors = False

    if len(post_message) < 1:
        flash("Message field must not be blank", "errors")
        errors = True

    if not errors:
        query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            "user_id": user_id,
            "message": post_message
        }
        mysql.query_db(query, data)
        flash("Message posted!", "success")
    return redirect('/wall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def post_comment(message_id):
    print "hit post_comment route"
    
    errors = False
    user_id = session['logged_id']
    comment = request.form['comment']

    if len(comment) < 1:
        flash("Comment field must not be blank", "errors")
        errors = True
    
    if not errors:
        query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"
        data = {
            "message_id": message_id,
            "user_id": user_id,
            "comment": comment
        }
        mysql.query_db(query, data)

        print user_id, message_id
    return redirect('/wall')

# @app.route('/remove_message', methods=['GET', 'POST'])
# def delete_message():
#     query = "DELETE FROM comments WHERE comments.message_id == :message_id"
#     data = {
#         'message_id': request.form['get_m_id']
#     }
#     mysql.query_db(query, data)
#     return redirect('/wall')

@app.route('/logout')
def logout():
    session.pop("logged_id")
    return redirect('/')

app.run(debug=True)