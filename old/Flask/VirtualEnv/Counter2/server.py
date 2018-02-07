from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "AJAOSDAPOSJD"

@app.route("/")
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    print session['counter']
    return render_template("index.html")

@app.route("/reset", methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect("/")

@app.route("/plustwo", methods=["POST"])
def plusTwo():
    print "adding another"
    session['counter'] += 1
    return redirect("/")

app.run(debug=True)