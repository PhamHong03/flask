from models.patient import Patient
from models.account import Account
from database import db
from datetime import datetime

class PatientController:
    @staticmethod
    def get_all_patient():
        return Patient.query.all()
    
    @staticmethod
    def get_patient_by_id(patient_id):
        return Patient.query.get(patient_id)
    
    @staticmethod
    def create_patient(data):
        account_id = data.get('account_id')
        
        account = Account.query.get(account_id)
        if not account:
            return None, "Tài khoản không tồn tại"

        existing_patient = Patient.query.filter_by(account_id=account_id).first()
        if existing_patient:
            return None, "Tài khoản này đã có hồ sơ bệnh nhân"

        new_patient = Patient(
            name=data['name'],
            day_of_birth=datetime.strptime(data['day_of_birth'], "%Y-%m-%d").date(),  
            gender=data['gender'],
            email=data['email'],
            phone=data['phone'],
            job=data['job'],
            address=data['address'],
            account_id=account_id
        )
        db.session.add(new_patient)
        db.session.commit()
        return new_patient, None