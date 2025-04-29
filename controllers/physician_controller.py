from models.physician import Physician
from database import db 
from models.account import Account

class PhysicianController:
    @staticmethod
    def get_all_physician():
        return Physician.query.all()
    
    @staticmethod
    def get_physician_by_id(physician_id):
        return Physician.query.get(physician_id)
    
    @staticmethod
    def create_physician(data):
        account_id = data.get('account_id')
        account = Account.query.get(account_id)
        if not account:
            return None, "Tài khoản không tồn tại"

        print("Data from Android:", data)
        new_physician = Physician(
            name=data['name'], 
            email=data['email'], 
            phone=data['phone'], 
            address=data['address'],
            gender=data['gender'] , 
            specialization_id=data['specialization_id'],
            education_id=data['education_id'],
            account_id=account_id
        )

        db.session.add(new_physician)
        db.session.commit()
        return new_physician