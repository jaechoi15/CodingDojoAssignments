from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

import re

app = Flask(__name__)
app.secret_key = "secretkey"
mysql = MySQLConnector(app, "friendsdb")

@app.route("/")
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", all_friends=friends)

@app.route("/friends", methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, now(), now())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route("/edit/<friend_id>")
def edit(friend_id):
    query = "SELECT * FROM friends WHERE id = :id"
    friend = mysql.query_db(query, {"id": friend_id})[0]
    print friend
    return render_template("edit.html", friend = friend)

@app.route("/update/<friend_id>", methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :new_first_name, last_name = :new_last_name, email = :new_email, created_at = now(), updated_at = now() WHERE id = :id"
    data = {
        'new_first_name': request.form['first_name'],
        'new_last_name': request.form['last_name'],
        'new_email': request.form['email'],
        'id': friend_id[0]
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route("/delete/<friend_id>")
def destroy(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {
        'id': friend_id[0]
    }
    mysql.query_db(query, data)
    return redirect("/")

app.run(debug=True)