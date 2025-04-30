from models.diagnose_disease import Diagnose_Disease
from database import db

class DiagnoseDiseaseController:
    @staticmethod
    def get_all_diagnose_disease():
        return Diagnose_Disease.query.all()
    
    @staticmethod
    def get_diagnose_disease_by_id(diagnose_disease_id):
        return Diagnose_Disease.query.get(diagnose_disease_id)
    