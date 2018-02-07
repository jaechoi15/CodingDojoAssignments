from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    errors = False
    if len(request.form["name"]) == 0:
        flash("Name field cannot be empty.")
        errors = True
    if len(request.form["comment"]) == 0:
        flash("Comment field cannot be empty.")
        errors = True
    if len(request.form["comment"]) > 120:
        flash("Comment field cannot be more than 120 characters.")
        errors = True
    if errors:
        return redirect("/")
    
    session["submission"] = request.form
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html", result=session["submission"])

app.run(debug=True)