from flask import Flask,render_template,redirect

app = Flask(__name__,template_folder='templates')



@app.route("/")
def homePage():
    return render_template("index.html")

app.run(debug=True)