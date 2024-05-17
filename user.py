from flask import jsonify, request
from __main__ import app, db
from fastapi.encoders import jsonable_encoder
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,relationship,joinedload

from dataClasses import *


@app.route('/api/users', methods=['GET'])
def getUsers():
     users = User.query.all()
     return (jsonable_encoder(users))


@app.route('/api/user/<int:id>', methods=['GET'])
def getUser(id):
     user =  User.query.get_or_404(id)
     return (jsonable_encoder(user))



@app.route('/api/user/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message' : 'delete success'}), 200


@app.route('/api/user/<int:id>', methods=['PUT'])
def updateUser(id):
    user = User.query.get_or_404(id)

    user.username=request.json['username']
    user.email=request.json['email']
    user.role=request.json['role']
    user.shelter_id=request.json['shelter_id']
    db.session.commit()
    return jsonify({'message' : 'update success'}), 200