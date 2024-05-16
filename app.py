
from flask import Flask,render_template,redirect,request,url_for  
import sqlalchemy
from sqlalchemy.orm import sessionmaker,relationship,joinedload
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/PurrfectMatch'
engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/PurrfectMatch')
Session = sessionmaker(bind=engine)

Base = declarative_base()

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    po_box = Column(String(255))
    googlemap_link = Column(Text)
    email = Column(String(255))
    phone_number = Column(String(255))
    description = Column(Text)
    website_link = Column(String(255))
    donation_link = Column(String(255))

    pets = relationship("Pet", back_populates="shelter")
class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    coat_length = Column(String(255))
    activity_level = Column(String(255))
    house_training = Column(String(255))
    pet_type = Column(String(255))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    health = Column(String(255))
    good_in_home = Column(Boolean)
    adoption_fee = Column(Integer)
    gender = Column(String(10))

    shelter = relationship("Shelter", back_populates="pets")
    pet_characteristics = relationship("PetCharacteristics", back_populates="pet")
    adoption_applications = relationship("AdoptionApplication", back_populates="pet")
    pet_description = relationship("PetDescription", uselist=False, back_populates="pet")
class PetDescription(Base):
    __tablename__ = 'pet_description'
    pet_id = Column(Integer, ForeignKey('pet.id'), primary_key=True)
    description = Column(Text)
    pet = relationship("Pet", back_populates="pet_description")
class PetCharacteristics(Base):
    __tablename__ = 'pet_characteristics'

    pet_id = Column(Integer, ForeignKey('pet.id'), primary_key=True)
    characteristic = Column(String(255), primary_key=True)

    pet = relationship("Pet", back_populates="pet_characteristics")
class Article(Base):
    __tablename__ = 'article'

    article_id = Column(Integer, primary_key=True, autoincrement=True)
    article_name = Column(String(255))
    image = Column(Text)
    article_info = Column(Text)
class AdoptionApplication(Base):
    __tablename__ = 'adoption_application'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(255))
    address = Column(String(255))
    description = Column(Text)
    pet_id = Column(Integer, ForeignKey('pet.id'))

    pet = relationship("Pet", back_populates="adoption_applications")
    replies = relationship("AdoptionApplicationReply", back_populates="application")
class AdoptionApplicationReply(Base):
    __tablename__ = 'adoption_application_reply'

    id = Column(Integer, primary_key=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('adoption_application.id'))
    reply_text = Column(Text)
    reply_date = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    application = relationship("AdoptionApplication", back_populates="replies")   
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)



app.config['SECRET_KEY'] = 'ali'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))   

@app.route("/", methods = ["GET","POST"])
def homePage():
    if request.method == "POST":
        searchURL = request.form["searchPet"]
        return redirect(f"/search/all/{searchURL}")
    return render_template("index.html", auth = current_user.is_authenticated , user = current_user)

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



@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/form")
def form():
    return render_template("form.html")

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
        login_user(new_user)
        return redirect(url_for('homePage'))
        
    return render_template('signup.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route('/managePets')
@login_required
def managePets():
    return redirect(url_for('homePage'))

@app.route('/editShelter')
@login_required
def editShelter():
    return redirect(url_for('homePage'))


app.run(debug=True)