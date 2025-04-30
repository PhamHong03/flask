from flask import Blueprint, request, jsonify   
from controllers.diagnose_disease_controller import DiagnoseDiseaseController  
from models.diagnose_disease import Diagnose_Disease 
from database import db

diagnose_disease_bp = Blueprint('diagnose_disease_bp', __name__)  

@diagnose_disease_bp.route('/diagnose_disease', methods=['GET'])   
def get_all_diagnose_disease():    
    diagnose_diseases = DiagnoseDiseaseController.get_all_diagnose_disease()    
    return jsonify([{"id":dd.id, "diagnose_disease_name": dd.diagnose_disease_name, "diagnose_disease_description":dd.diagnose_disease_description, "category_disease_id": dd.category_disease_id} for dd in diagnose_diseases])

@diagnose_disease_bp.route('/diagnose_disease/<int:diagnose_disease_id>')
def get_diagnose_disease_by_id(diagnose_disease_id):

    diagnose_disease = DiagnoseDiseaseController.get_diagnose_disease_by_id(diagnose_disease_id)
    return jsonify({"id": diagnose_disease.id, "diagnose_disease_name": diagnose_disease.diagnose_disease_name, "diagnose_disease_description": diagnose_disease.category_disease_id})

@diagnose_disease_bp.route('/diagnose_disease', methods=['POST'])
def create_diagnose_disease():
    data = request.get_json()
    
    if not data or "diagnose_disease_name" not in data or "diagnose_disease_description" not in data or "category_disease_id" not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_diagnose = Diagnose_Disease(
        diagnose_disease_name=data["diagnose_disease_name"],
        diagnose_disease_description=data["diagnose_disease_description"],
        category_disease_id=data["category_disease_id"]
    )
    
    db.session.add(new_diagnose)
    db.session.commit()
    
    return jsonify({"message": "Diagnose disease created successfully"}), 201

