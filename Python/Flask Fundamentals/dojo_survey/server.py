from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    session['submission'] = request.form
    
    errors = False

    if len(request.form['name']) < 1:
        flash("Name field cannot be empty.")
        errors = True

    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty.")
        errors = True
    
    if len(request.form['comment']) > 120:
        flash("Comment field must not be more than 120 characters.")
        errors = True

    if errors == True:
        return redirect('/')
    else:
        return render_template("result.html", submission=session['submission'])

# @app.route('/result', methods=["POST"])
# def result():
#     name = request.form['name']
#     location = request.form['location']
#     language = request.form['language']
#     comment = request.form['comment']
#     return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)