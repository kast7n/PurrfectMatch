from flask import jsonify, request
from __main__ import app, db
from fastapi.encoders import jsonable_encoder
from dataClasses import *



@app.route('/api/pets', methods=['GET'])
def getPets():
     pets = Pet.query.all()
     return (jsonable_encoder(pets))

@app.route('/api/pets/shelter/<int:shelterID>', methods=['GET'])
def getShelterPets(shelterID):
     pets = Pet.query.filter(Pet.shelter_id == shelterID).all()
     return (jsonable_encoder(pets))

@app.route('/api/pet/<int:id>', methods=['GET'])
def getPet(id):
     pet = Pet.query.get_or_404(id)
     return (jsonable_encoder(pet))

@app.route('/api/pet', methods=['POST'])
def addPet():
    pet = Pet(name=request.json['name'], coat_length=request.json['coat_length'],activity_level=request.json['activity_level'],house_training=request.json['house_training'],pet_type=request.json['pet_type'],           
                shelter_id=request.json['shelter_id'], health=request.json['health'],good_in_home=request.json['good_in_home'],adoption_fee=request.json['adoption_fee'],gender=request.json['gender'])
    db.session.add(pet)
    db.session.commit()
    pet_description = PetDescription(pet_id=pet.id, description=request.json['description'])
    db.session.add(pet_description)
    characteristicsList = request.json['characteristic'].split()
    for charact in characteristicsList:
        petCharacteristics = PetCharacteristics(pet_id=pet.id,characteristic = charact)
        db.session.add(petCharacteristics)
    db.session.commit()
    return jsonable_encoder(pet), 201

@app.route('/api/pet/<int:id>', methods=['DELETE'])
def deletePet(id):
    pet = Pet.query.get_or_404(id)
    charac = PetCharacteristics.query.filter(PetCharacteristics.pet_id == id).all()
    descrip = PetDescription.query.filter(PetDescription.pet_id == id).all()
    db.session.delete(pet)
    for i in charac:
        db.session.delete(i)
    if len(descrip) > 0:
        db.session.delete(descrip[0])

    db.session.commit()
    return jsonify({'message' : 'delete success'}), 200


@app.route('/api/pet/<int:id>', methods=['PUT'])
def updatePet(id):
    pet = Pet.query.get_or_404(id)
    pet.name=request.json['name']
    pet.coat_length=request.json['coat_length']
    pet.activity_level=request.json['activity_level']
    pet.house_training=request.json['house_training']
    pet.pet_type=request.json['pet_type'],           
    pet.shelter_id=request.json['shelter_id']
    pet.health=request.json['health']
    pet.good_in_home=request.json['good_in_home']
    pet.adoption_fee=request.json['adoption_fee']
    pet.gender=request.json['gender']
    db.session.commit()
    return jsonify({'message' : 'update success'}), 200
