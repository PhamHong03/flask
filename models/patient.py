from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    day_of_birth = db.Column(db.Date, nullable=False) 
    gender = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    job = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), unique=True, nullable=False)    

    # Quan hệ với ApplicationForm
    account = db.relationship('Account', backref=db.backref('patient', uselist=False))
    # application_forms = db.relationship('ApplicationForm', back_populates='patient', cascade="all, delete-orphan")
    

    def __init__(self, name, day_of_birth, gender, email, phone, job, address, account_id):
        self.name = name
        self.day_of_birth = day_of_birth
        self.gender = gender
        self.email = email
        self.phone = phone
        self.job = job
        self.address = address
        self.account_id = account_id    