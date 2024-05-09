
from flask import Flask,render_template,redirect,request
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_,and_


app = Flask(__name__,template_folder='templates')

Base = sqlalchemy.orm.declarative_base()

class Pet(Base):
    __tablename__ = 'pet'
    petID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    petName = sqlalchemy.Column(sqlalchemy.String(35))
    petPicture = sqlalchemy.Column(sqlalchemy.String(255))
    petType = sqlalchemy.Column(sqlalchemy.String(15))

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/PurrfectMatch')
Session = sessionmaker(bind=engine)

@app.route("/", methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchURL = request.form["searchPet"]
        return redirect(f"/search/all/{searchURL}")
    return render_template("index.html")

@app.route("/search/<type>/<name>")
def search(type,name):
    pets = []
    session = Session()
    if type == "all":
        condition = Pet.petName == name if name != "all" else True
    else:
        condition = Pet.petType == type if name == "all" else and_(Pet.petName == name, Pet.petType == type)

    pets = session.query(Pet).filter(condition).all()
    
    session.close()

    return render_template("searchResults.html",petType = type,petName = name,filteredPets = pets)
@app.route('/articles')
def articles():
    return render_template('articles.html')

app.run(debug=True)