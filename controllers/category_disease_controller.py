from models.category_disease import Category_Disease

from database import db

class CategoryDiseaseController:
    @staticmethod
    def get_all_category_disease():
        return Category_Disease.query.all()
    
    @staticmethod   
    def get_category_disease_by_id(category_disease_id):
        return Category_Disease.query.get(category_disease_id)