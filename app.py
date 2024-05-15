
from flask import Flask,render_template,redirect,request    
import sqlalchemy
from sqlalchemy.orm import sessionmaker,relationship,joinedload,declarative_base
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/PurrfectMatch'
Base = declarative_base()
engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/PurrfectMatch')
Session = sessionmaker(bind=engine)
db = SQLAlchemy(app)

from dataClasses import *

import shelter
import pet






@app.route("/", methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchURL = request.form["searchPet"]
        return redirect(f"/search/all/{searchURL}")
    return render_template("index.html")

@app.route("/search/<type>/<name>")
def search(type,name):
    page = request.args.get('page',1,type=int)
    per_page = 25
    start = (page - 1) * per_page
    end = start + per_page
    

    pets = []
    session = Session()
    if type == "all":
        condition = Pet.name == name if name != "all" else True
    else:
        condition = Pet.pet_type == type if name == "all" else and_(Pet.name == name, Pet.pet_type == type)

    pets = session.query(Pet, Shelter.name, PetDescription.description).\
    join(Shelter).\
    join(PetDescription, PetDescription.pet_id == Pet.id).\
    options(joinedload(Pet.shelter)).\
    filter(condition).all()
    total_pages = (len(pets) + per_page - 1) // per_page
    pets_on_page = pets[start:end]



    session.close()

    return render_template("searchResults.html",petType = type,petName = name,filteredPets = pets_on_page,total_pages = total_pages,page = page)
@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route("/pet/<petID>")
def pet(petID):
    pet_and_shelter_info = []
    pet_characteristics = []
    session = Session()
    pet_and_shelter_info = session.query(Pet, Shelter,PetDescription) \
    .join(Shelter) \
    .join(PetDescription) \
    .filter(Pet.id == petID) \
    .all()
    pet_characteristics = session.query(PetCharacteristics).filter(PetCharacteristics.pet_id == petID).all()
    session.close()
    characteristics_str = ', '.join([char.characteristic for char in pet_characteristics])
    pet_and_shelter_info.append(characteristics_str)
    print(pet_and_shelter_info[1])

    return render_template("pet.html",ID = petID,pet_and_shelter_info = pet_and_shelter_info)

@app.route("/shelter/<shelterID>")
def shelter(shelterID):
    
    session = Session()
    curr_shelter = session.query(Shelter).filter(Shelter.id == shelterID).all()
    print(curr_shelter)
    return render_template("shelter.html",shelter = curr_shelter)

@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/form")
def form():
    return render_template("form.html")

app.run(debug=True)