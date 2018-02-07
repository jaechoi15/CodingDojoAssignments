from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def result():
    name = request.form['name']
    dojo_loc = request.form['dojo_loc']
    favorite_lang = request.form['favorite_lang']
    comment = request.form['comment']

    return render_template('result.html', name=name, dojo_loc=dojo_loc, favorite_lang=favorite_lang, commment=comment)

app.run(debug=True)