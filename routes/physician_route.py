from flask import Blueprint, request, jsonify   
from controllers.physician_controller import PhysicianController
from models.physician import Physician
# from models.patient import Patient
# from models.application_form import ApplicationForm
# from models.medical_history import MedicalHistory
from models.room import Room
from database import db

physician_bp = Blueprint('physician_bp', __name__)

@physician_bp.route('/physicians', methods=['GET'])
def get_all_physician():
    physicians = PhysicianController.get_all_physician()

    if not physicians:
        return jsonify({"message": "No physicians found"}), 404

    return jsonify([
        {
            "id": p.id, 
            "name": p.name, 
            "email": p.email, 
            "phone": p.phone, 
            "address": p.address,
            "gender": p.gender,
            "specialization_id": p.specialization_id,
            "education_id": p.education_id,
            "account_id": p.account_id
        }
        for p in physicians
    ]), 200  

@physician_bp.route('/physicians/<int:physician_id>', methods=['GET'])  
def get_physician(physician_id):
    physician = PhysicianController.get_physician_by_id(physician_id) 
    if physician is None:
        return jsonify({"message": "Physician not found"}), 404

    return jsonify({
        "id": physician.id, 
        "name": physician.name, 
        "email": physician.email, 
        "phone": physician.phone, 
        "address": physician.address,
        "gender": physician.gender,
        "specialization_id": physician.specialization_id,
        "education_id": physician.education_id,
        "account_id": physician.account_id
    }), 200


@physician_bp.route('/physicians', methods=['POST'])
def create_physician():
    data = request.get_json()
    print("Received data from Android:", data)
    new_physician = PhysicianController.create_physician(data)
    return jsonify({
        "id": new_physician.id,
        "name": new_physician.name,
        "email": new_physician.email,
        "phone": new_physician.phone,
        "address": new_physician.address,
        "gender": new_physician.gender,
        "specialization_id": new_physician.specialization_id,
        "education_id": new_physician.education_id,
        "account_id": new_physician.account_id
    }), 201
        
@physician_bp.route('/physicians/account/<int:account_id>', methods=['GET'])
def get_physicians_by_account_id(account_id):
    physician = Physician.query.filter_by(account_id=account_id).first()
    if not physician:
        return jsonify({"message": "Physician not found"}), 404
    
    return jsonify({
        "id": physician.id,
        "name": physician.name,
        "email": physician.email,
        "phone": physician.phone,
        "address": physician.address,
        "gender": physician.gender,
        "specialization_id": physician.specialization_id,
        "education_id": physician.education_id,
        "account_id": physician.account_id
    }), 200

# @physician_bp.route('/physician/<int:physician_id>/patients', methods=['GET'])
# def get_patients_by_physician(physician_id):
#     print(f"🔍 Requested physician_id: {physician_id}")

#     patients = db.session.query(
#         Patient, 
#         ApplicationForm.id, 
#         ApplicationForm.application_form_date, 
#         ApplicationForm.content ,
#         ApplicationForm.room_id
    
#     )\
#     .join(ApplicationForm, ApplicationForm.patient_id == Patient.id)\
#     .join(MedicalHistory, ApplicationForm.medical_history_id == MedicalHistory.id)\
#     .join(Room, ApplicationForm.room_id == Room.id)\
#     .filter(MedicalHistory.physician_id == physician_id).all()

#     if not patients:
#         return jsonify({"error": f"No patients found for physician_id: {physician_id}"}), 404

#     patient_list = [
#         {
#             "patient_id": p[0].id,
#             "patient_name": p[0].name,
#             "application_form_id": p[1],  
#             "application_form_date": p[2],
#             "application_form_content": p[3] , 
#             "application_form_room_id": p[4]
#         }
#         for p in patients
#     ]

#     return jsonify(patient_list)


