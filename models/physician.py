from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class Physician(db.Model):
    __tablename__ = 'physicians'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True) 
    phone = db.Column(db.String(255), nullable=False, unique=True)  
    address = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(100), nullable=False)    
    specialization_id = db.Column(db.Integer, db.ForeignKey('specializations.id', ondelete="CASCADE"), nullable=False)
    education_id = db.Column(db.Integer, db.ForeignKey('educations.id', ondelete="CASCADE"), nullable=False)   
    specialization = db.relationship('Specialization', back_populates='physicians')
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), unique=True, nullable=False) 

    # Thêm quan hệ với Education
    education = db.relationship('Education', back_populates='physicians')
    account = db.relationship('Account', backref=db.backref('physician', uselist=False))
    # medical_histories = db.relationship('MedicalHistory', back_populates='physician', cascade="all, delete-orphan")
    # images = db.relationship('Images', back_populates='physician', cascade="all, delete-orphan")

    def __init__(self, name, email, phone, address, gender, education_id, specialization_id, account_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address  
        self.gender = gender        
        self.education_id = education_id
        self.specialization_id = specialization_id
        self.account_id = account_id
