from flask_mysqldb import MySQL
from flask import jsonify
from database import db

# mysql = MySQL()

class Specialization(db.Model):
    __tablename__ = 'specializations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True) 
    quantity_patient = db.Column(db.Integer, nullable=False, default=0)  
    
    physicians = db.relationship('Physician', back_populates='specialization', cascade="all, delete")

    def __init__(self, name, quantity_patient=0):
        self.name = name
        self.quantity_patient = quantity_patient  
