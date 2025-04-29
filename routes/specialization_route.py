from flask import Blueprint, request, jsonify
from controllers.specialization_controller import SpecializationController

specialization_bp = Blueprint('specialization_bp', __name__)

@specialization_bp.route('/specializations', methods=['GET'])
def get_all_specialization():
    specializations = SpecializationController.get_all_specialization()
    return jsonify([{"id":s.id, "name": s.name, "quantity_patient":s.quantity_patient} for s in specializations])


@specialization_bp.route('/specializations/<int:specialization_id>', methods=['GET'])
def get_specialization_by_id(specialization_id): 
    spec = SpecializationController.get_specialization_by_id(specialization_id)
    if spec:
        return jsonify({"id": spec.id, "name":  spec.name, "quantity_patient": spec.quantity_patient})

    return jsonify({"message": "Specialization not found"}), 404


@specialization_bp.route('/specializations',methods=['POST'])
def create_specialization():
    data = request.json
    specialization = SpecializationController.create_specialization(data)
    return jsonify({"message": "Specialization created",  "id":specialization.id}), 201


@specialization_bp.route('/specializations/<int:specialization_id>', methods=['PUT'])
def update_specialization(specialization_id):
    data = request.json
    specialization = SpecializationController.update_specialization(specialization_id, data)
    if specialization:
        return jsonify({"message": "Specialization updated"})
    return jsonify({"message": "Specialization not found"}) , 404

@specialization_bp.route('/specialization_id', methods=['DELETE'])
def delete_specialization(specialization_id):
    specialization = SpecializationController.delete_specialization(specialization_id)

    if specialization:
        return jsonify({"message": "Specialization deleted"})
    
    return jsonify({"message": "Specialization not found"}), 405