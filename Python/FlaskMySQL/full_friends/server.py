from flask import Flask, redirect, request, render_template, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "secret"
mysql = MySQLConnector(app, 'fullfriends')
EMAIL_REGEX = re.compile(r'^[a-zA-z0-9\.\+_-]+@[a-zA-z0-9\._+]+\.[a-zA-Z]*$')

# Display All Friends
@app.route('/')
def index():
    print "hit index route"
    query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at,'%m/%d/%Y %I:%i %p') AS created_at FROM full_friends"
    all_friends = mysql.query_db(query)
    return render_template("index.html", all_friends=all_friends)

# Add Friend
@app.route('/create', methods=['POST'])
def create():
    print "hit create route"
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    errors = False

    if not errors: 
        query = "INSERT INTO full_friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, now(), now())"
        db = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        mysql.query_db(query,db)

        flash("{} {} was added successfully!".format(first_name, last_name), "success")
    return redirect('/')

# View Edit Page
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    print "hit edit route"
    query = "SELECT * FROM full_friends WHERE id = :id"
    db = {
        "id":friend_id
    }
    friend = mysql.query_db(query,db)

    print "ID =", friend_id
    return render_template("edit.html", friend=friend)

# Update Friend
@app.route('/friends/<friend_id>', methods=['POST'] )
def update(friend_id):
    print "hit update route"
    upd_first_name = request.form['upd_first_name']
    upd_last_name = request.form['upd_last_name']
    upd_email = request.form['upd_email']

    query = "UPDATE full_friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    db = {
        "first_name":upd_first_name,
        "last_name":upd_last_name,
        "email":upd_email,
        "id":friend_id
    }
    mysql.query_db(query,db)
    return redirect('/')

# Delete Friend
@app.route('/friends/<friend_id>/delete')
def destroy(friend_id):
    print "hit destroy route"
    query = "DELETE FROM full_friends WHERE id = :friend_id"
    db = {
        "friend_id":friend_id
    }
    mysql.query_db(query,db)
    return redirect('/')

app.run(debug=True)