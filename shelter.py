from flask import jsonify, request
from __main__ import app, db
from fastapi.encoders import jsonable_encoder
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,relationship,joinedload


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
   # pets = relationship("Pet", back_populates="shelter")

@app.route('/api/shelters', methods=['GET'])
def getShelters():
     shelter = Shelter.query.all()
     return (jsonable_encoder(shelter))


@app.route('/api/shelters/<int:id>', methods=['GET'])
def getShelter(id):
     shelter =  Shelter.query.get_or_404(id)
     return (jsonable_encoder(shelter))

@app.route('/api/shelters', methods=['POST'])
def addshelter():
      shelter = Shelter(name=request.json['name'], address=request.json['address'],po_box=request.json['po_box'],\
                        googlemap_link=request.json['googlemap_link'],email=request.json['email'],phone_number=request.json['phone_number'],\
                        description=request.json['description'],website_link=request.json['website_link'],donation_link=request.json['donation_link'])
      db.session.add(shelter)
      db.session.commit()
      return jsonable_encoder(shelter), 201


@app.route('/api/shelters/<int:id>', methods=['DELETE'])
def deleteShelter(id):
    shelter = Shelter.query.get_or_404(id)
    db.session.delete(shelter)
    db.session.commit()
    return jsonify({'message' : 'delete success'}), 200


@app.route('/api/shelters/<int:id>', methods=['PUT'])
def updateShelter(id):
    shelter = Shelter.query.get_or_404(id)

    shelter.name=request.json['name']
    shelter.address=request.json['address']
    shelter.po_box=request.json['po_box']
    shelter.googlemap_link=request.json['googlemap_link']
    shelter.email=request.json['email']
    shelter.phone_number=request.json['phone_number']
    shelter.description=request.json['description']
    shelter.website_link=request.json['website_link']
    shelter.donation_link=request.json['donation_link']
    db.session.commit()
    return jsonify({'message' : 'update success'}), 200