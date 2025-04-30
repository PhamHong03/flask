from flask import Blueprint, request, jsonify
from controllers.category_disease_controller import CategoryDiseaseController

category_disease_bp = Blueprint('category_disease_bp', __name__)

@category_disease_bp.route('/category_disease', methods=['GET'])
def get_all_category_disease():
    category_diseases = CategoryDiseaseController.get_all_category_disease()
    return jsonify([{"id":cd.id, "category_disease_name": cd.category_disease_name, "category_disease_description":cd.category_disease_description} for cd in category_diseases])


@category_disease_bp.route('/category_diseases/<int:category_disease_id>', methods=['GET'])
def get_category_disease_by_id(category_disease_id):
    category_disease = CategoryDiseaseController.get_category_disease_by_id(category_disease_id)
    return jsonify([{"id":cd.id, "category_disease_name": cd.category_disease_name, "category_disease_description":cd.category_disease_description} for cd in category_disease])