from flask import jsonify, request
from __main__ import app, db
from fastapi.encoders import jsonable_encoder
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,relationship,joinedload

from dataClasses import *


@app.route('/api/applications/<int:shelterID>', methods=['GET'])
def getApplications(shelterID):
     applications = db.session.query(
     AdoptionApplication,
     Pet.name
     ).join(Pet).filter(Pet.shelter_id == shelterID).all()

     application_data = []
     for application, pet_name in applications:
          application_data.append({
               'application_id': application.id,
               'username': application.username,
               'email': application.email,
               'phone_number': application.phone_number,
               'description': application.description,
               'address': application.address,
               'pet_name': pet_name
          })

    
     return (jsonify(application_data))


@app.route('/api/applications/<int:id>', methods=['DELETE'])
def rejectApplication(id):
    applications = AdoptionApplication.query.get_or_404(id)
    db.session.delete(applications)
    db.session.commit()
    return jsonify({'message' : 'Rejected successfully'}), 200

@app.route('/api/applications/accept/<int:id>', methods=['POST'])
def acceptApplication(id):
     applications = AdoptionApplication.query.get_or_404(id)
     pet = Pet.query.get_or_404(applications.pet_id)

     applicationReply = AdoptionApplicationReply(application_id = id,pet_id = applications.pet_id,reply_text = "Your request have been accepted",user_id = applications.user_id)
     
     db.session.add(applicationReply)
     
     #db.session.delete(applications)
     #db.session.delete(pet)
     db.session.commit()
    
     return jsonify({'message' : 'Accepted successfully'}), 201  

@app.route('/api/notifications/<int:id>', methods=['GET'])
def notifications(id):
     applicationReply = AdoptionApplicationReply.query.filter(AdoptionApplicationReply.user_id == 8).all()
     print(applicationReply)
     pet= []
     for app in applicationReply:
          pet.append(Pet.query.filter(Pet.id == app.pet_id).all())
     print(pet)
     counter = 0
     application_data = []
     for application in applicationReply:
          application_data.append({
               'application_id': application.id,
               'reply_text': application.reply_text,
               'reply_date': application.reply_date,
               'pet_name': pet[counter][0].name
          })
          counter+=1
     
     
     return (jsonify(application_data))
