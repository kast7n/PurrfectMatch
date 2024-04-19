from flask import Flask,render_template,redirect,request

app = Flask(__name__,template_folder='templates')



@app.route("/", methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchURL = request.form["searchPet"]
        return redirect(f"/search/{searchURL}")
    return render_template("index.html")

@app.route("/search/<name>")
def search(name):
    return render_template("searchResults.html",petName = name)

app.run(debug=True)