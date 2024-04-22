from flask import Flask,render_template,redirect,request
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__,template_folder='templates')

Base = declarative_base()

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
        return redirect(f"/search/All/{searchURL}")
    return render_template("index.html")

@app.route("/search/<type>/<name>")
def search(type,name):
    pets = []
    session = Session()
    if type == "all":    
        if name == "all":
            pets = session.query(Pet).all()
        else:
            pets = session.query(Pet).filter(Pet.petName == name).all()
    else:
    
        if name == "all":
            pets = session.query(Pet).filter(Pet.petType == type).all()
        else:
            pets = session.query(Pet).filter(Pet.petName == name, Pet.petType == type).all()
    
    session.close()

    return render_template("searchResults.html",petType = type,petName = name,filteredPets = pets)

app.run(debug=True)