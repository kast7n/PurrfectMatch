from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,relationship,joinedload
from __main__ import db
from flask_login import UserMixin


class Shelter(db.Model):
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

class Pet(db.Model):
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

class PetDescription(db.Model):
    __tablename__ = 'pet_description'
    pet_id = Column(Integer, ForeignKey('pet.id'), primary_key=True)
    description = Column(Text)
    pet = relationship("Pet", back_populates="pet_description",cascade='delete')

class PetCharacteristics(db.Model):
    __tablename__ = 'pet_characteristics'
    pet_id = Column(Integer, ForeignKey('pet.id'), primary_key=True)
    characteristic = Column(String(255), primary_key=True)
    pet = relationship("Pet", back_populates="pet_characteristics",cascade='delete')

class Article(db.Model):
    __tablename__ = 'article'

    article_id = Column(Integer, primary_key=True, autoincrement=True)
    article_name = Column(String(255))
    image = Column(Text)
    article_info = Column(Text)

class AdoptionApplication(db.Model):
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

class AdoptionApplicationReply(db.Model):
    __tablename__ = 'adoption_application_reply'

    id = Column(Integer, primary_key=True, autoincrement=True)
    application_id = Column(Integer, ForeignKey('adoption_application.id'))
    reply_text = Column(Text)
    reply_date = Column(TIMESTAMP, server_default=" ")

    application = relationship("AdoptionApplication", back_populates="replies")   

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    shelter_id = Column(Integer, ForeignKey('shelter.id', ondelete='CASCADE'))
    shelter = relationship('Shelter')

