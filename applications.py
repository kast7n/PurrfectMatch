from flask import jsonify, request
from __main__ import app, db
from fastapi.encoders import jsonable_encoder
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey,and_,Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,relationship,joinedload

from dataClasses import *


@app.route('/api/applications', methods=['GET'])
def getApplications():
     applications = AdoptionApplication.query.all()
     return (jsonable_encoder(applications))


@app.route('/api/applications/<int:id>', methods=['DELETE'])
def rejectApplication(id):
    applications = AdoptionApplication.query.get_or_404(id)
    db.session.delete(applications)
    db.session.commit()
    return jsonify({'message' : 'Rejected successfully'}), 200