from flask import Flask,render_template,redirect,request,url_for  
import sqlalchemy
from sqlalchemy.orm import sessionmaker,relationship,joinedload,declarative_base
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text,or_, func
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/PurrfectMatch'

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/PurrfectMatch')
Session = sessionmaker(bind=engine)
Base = declarative_base()
db = SQLAlchemy(app)

from dataClasses import *

import shelter
import pet
import user
import applications

login_manager = LoginManager(app)


app.config['SECRET_KEY'] = 'ali'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   


@app.route("/", methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchURL = request.form["searchPet"]
        return redirect({{ url_for('search', type='all', name=searchURL, characteristic='all', coat='all', activity='all', house='all') }})
    session = Session()

    pets = session.query(Pet, Shelter.name, PetDescription.description).\
        join(Shelter).\
        join(PetDescription, PetDescription.pet_id == Pet.id).\
        options(joinedload(Pet.shelter)).\
        join(PetCharacteristics, PetCharacteristics.pet_id == Pet.id)\
        .order_by(func.random()).limit(3).all()
    return render_template("index.html", auth = current_user.is_authenticated , user = current_user, pets = pets)

@app.route("/search/<type>/<name>/<characteristic>/<coat>/<activity>/<house>")
def search(type, name, characteristic, coat, activity, house):
    page = request.args.get('page', 1, type=int)
    per_page = 25
    start = (page - 1) * per_page
    end = start + per_page

    session = Session()

    # Define the conditions
    conditions = []
    if type != "all":
        conditions.append(Pet.pet_type == type)
    if name != "all":
        conditions.append(Pet.name == name)
    if characteristic != "all":
        conditions.append(PetCharacteristics.characteristic == characteristic)
    if coat != "all":
        conditions.append(Pet.coat_length == coat)
    if activity != "all":
        conditions.append(Pet.activity_level == activity)
    if house != "all":
        conditions.append(Pet.house_training == house)

    # Build the final condition
    condition = and_(*conditions) if conditions else True

    # Fetch the filtered pets
    pets = session.query(Pet, Shelter.name, PetDescription.description).\
        join(Shelter).\
        join(PetDescription, PetDescription.pet_id == Pet.id).\
        options(joinedload(Pet.shelter)).\
        join(PetCharacteristics, PetCharacteristics.pet_id == Pet.id).\
        filter(condition)\
       .order_by(func.random()).all()

    total_pages = (len(pets) + per_page - 1) // per_page
    pets_on_page = pets[start:end]
    
    session.close()

    return render_template("searchResults.html", petType=type, petName=name, petCharacteristic=characteristic,
                           petCoat=coat, petActivity=activity, petHouse=house, filteredPets=pets_on_page,
                           total_pages=total_pages, page=page)

@app.route('/articles')
def articles():
    session = Session()
    articles = session.query(Article).all()
    return render_template('articles.html', auth = current_user.is_authenticated,article = articles)

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

    return render_template("pet.html",ID = petID,pet_and_shelter_info = pet_and_shelter_info, auth = current_user.is_authenticated )



@app.route("/shelter/<shelterID>")
def shelter(shelterID):
    
    session = Session()
    curr_shelter = session.query(Shelter).filter(Shelter.id == shelterID).all()
    session.close()
    
    return render_template("shelter.html",shelter = curr_shelter, auth = current_user.is_authenticated )



@app.route("/article/<articleID>")
def article(articleID):
    session = Session()
    article = session.query(Article).filter(Article.article_id == articleID).all()
    return render_template("article.html", auth = current_user.is_authenticated,article = article )

@app.route("/form/<petID>" , methods=['GET', 'POST'])
def form(petID):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        address = request.form['address']
        occupation = request.form['occupation']
        extra = request.form['extra']
        new_application = AdoptionApplication(
            username=name,
            email=email,
            phone_number=phone,
            address=address,
            description=extra,
            pet_id= petID
        )
        db.session.add(new_application)
        db.session.commit()
        db.session.close()
        return redirect(url_for('homePage'))
    return render_template("form.html", auth = current_user.is_authenticated ,petID=petID)


@app.route("/pet/add")
def addPetForm():
    return render_template("petForm.html", auth = current_user.is_authenticated )

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('homePage'))
        
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    if request.method == 'POST':
        new_user=User(email = request.form['email'], username = request.form['username'], password = generate_password_hash(request.form['password']), role="user")
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        login_user(new_user)
        return redirect(url_for('homePage'))
        
    return render_template('signup.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route('/managePets')
def managePets():
    if current_user.is_authenticated and current_user.role != "user":
        return render_template('managePets.html',shelter_id = current_user.shelter_id,user = current_user, auth = current_user.is_authenticated )
    return redirect(url_for('homePage'))
@app.route('/manageShelters')
def manageShelters():
    if current_user.is_authenticated and current_user.role == "admin":
        return render_template('manageShelters.html',shelter_id = current_user.shelter_id,user = current_user, auth = current_user.is_authenticated)
    return redirect(url_for('homePage'))


@app.route('/manageUsers')
def manageUsers():
    if current_user.is_authenticated and current_user.role == "admin":
        return render_template('manageUsers.html',user = current_user,management = "manageUsers", auth = current_user.is_authenticated )
    return redirect(url_for('homePage'))



@app.route('/notification')
@login_required
def notification():
    return render_template('manageNotitications.html',user = current_user,management = "manageApplications", auth = current_user.is_authenticated )

@app.route('/manageApplications')
@login_required
def manageApplications():
    if current_user.is_authenticated and current_user.role == "shelter":
        return render_template('manageApplications.html',user = current_user,management = "manageApplications", auth = current_user.is_authenticated )
    return redirect(url_for('homePage'))


if __name__ == '__main__':
    app.run(debug=True)