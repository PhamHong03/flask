# from flask import Blueprint, jsonify
# from models.specialization import Specialization

# specialization_bp = Blueprint("specialization", __name__)

# @specialization_bp.route("/chuyenkhoa", methods=["GET"])
# def get_chuyen_khoa():
#     return jsonify(Specialization.get_all())


from models.specialization import Specialization
from database import db

class SpecializationController:
    @staticmethod
    def get_all_specialization():
        return Specialization.query.all()
    

    @staticmethod
    def get_specialization_by_id(specialization_id):
        return Specialization.query.get(specialization_id)
    
    @staticmethod
    def create_specialization(data):
        new_specialization = Specialization(name=data['name'], quantity_patient=data['quantity_patient'])
        db.session.add(new_specialization)
        db.session.commit()
        return new_specialization
    
    @staticmethod
    def update_specialization(specialization_id, data):
        specialization = Specialization.query.get(specialization_id)
        if specialization:
            specialization.name = data['name']
            specialization.quantity_patient = data['quantity_patient']
            db.session.commit()
        return specialization
    

    @staticmethod
    def delete_specialization(specialization_id):
        specialization = Specialization.query.get(specialization_id)
    
        if specialization:
            db.session.delete(specialization)
            db.session.commit()
        return specialization
    
    