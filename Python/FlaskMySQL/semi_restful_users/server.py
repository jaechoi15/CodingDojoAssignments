from flask import Flask, request, redirect, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, "fullfriends")

# display all the users
@app.route('/users')
def index():
    query = "SELECT id, CONCAT(first_name, ' ',last_name) as full_name, email, DATE_FORMAT(created_at,'%m/%d/%Y %I:%i %p') AS created_at FROM fullfriends.full_friends"
    all_users = mysql.query_db(query)
    print "*"*100
    print all_users
    return render_template("index.html", all_users=all_users)

# displays a form allowing users to create a new user
@app.route('/users/new')
def new():
    return render_template("new.html")

# insert a new user record into the database
@app.route('/create', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    query = "INSERT INTO `fullfriends`.`full_friends` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES (:first_name, :last_name, :email, now(), now())"
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    mysql.query_db(query, data)

    query = "SELECT id FROM full_friends WHERE first_name = :first_name AND last_name = :last_name AND email = :email"
    user_id = mysql.query_db(query, data)
    user_id = user_id[0]['id']

    return redirect('/users/'+ str(user_id))

# display a form allowing the user to edit an existing user with the given id
@app.route('/users/<user_id>/edit')
def edit(user_id):
    query = "SELECT id, first_name, last_name, email FROM full_friends WHERE id = :user_id"
    data = {
        "user_id": user_id
    }
    user = mysql.query_db(query, data)
    username = user[0]

    return render_template("edit.html", user_id=user_id, username=username)

# displays the info for the selected user
@app.route('/users/<user_id>')
def show(user_id):
    query = "SELECT id, CONCAT(first_name, ' ',last_name) as full_name, email, DATE_FORMAT(created_at,'%m/%d/%Y %I:%i %p') AS created_at FROM full_friends WHERE id = :user_id"
    data = {
        "user_id": user_id
    }
    user = mysql.query_db(query, data)
    user = user[0]

    return render_template("show.html", user=user)

# process the submitted form from the edit route
@app.route('/users/<user_id>', methods=['POST'])
def update(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    query = "UPDATE full_friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :user_id"
    data = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    mysql.query_db(query, data)

    return redirect('/users/'+ str(user_id))

# remove the selected user
@app.route('/users/<user_id>/destroy')
def destroy(user_id):
    query = "DELETE FROM full_friends WHERE id = :user_id"
    data = {
        "user_id": user_id
    }
    mysql.query_db(query, data)
    return redirect('/users')

app.run(debug=True)