import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PetTable(Base):
    __tablename__ = 'pet'
    petID = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    petName = sqlalchemy.Column(sqlalchemy.String(35))
    petPicture = sqlalchemy.Column(sqlalchemy.String(255))
    petType = sqlalchemy.Column(sqlalchemy.String(15))

engine = sqlalchemy.create_engine('mysql+pymysql://root:12345@127.0.0.1:3306/PurrfectMatch')
Session = sessionmaker(bind=engine)
session = Session()

pets = session.query(PetTable).all()

for pet in pets:
    print("Pet ID:", pet.petID)
    print("Pet Name:", pet.petName)
    print("Pet Picture:", pet.petPicture)
    print("Pet Type:", pet.petType)
    print("-----------------------")

session.close()