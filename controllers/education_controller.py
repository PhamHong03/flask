
from models.education import Education
from database import db

class EducationController:
    @staticmethod
    def get_all_education():
        return Education.query.all()
    

    @staticmethod
    def get_education_by_id(education_id):
        return Education.query.get(education_id)
    
    @staticmethod
    def create_education(data):
         new_education = Education(name=data['name'])
         db.session.add(new_education)
         db.session.commit()
         return new_education
    
    @staticmethod
    def update_education(education_id, data):
        education = Education.query.get(education_id)
        if education:
            education.name = data['name']
            db.session.commit()
            return education
        return None
    
    @staticmethod 
    def delete_education(education_id):
        education = Education.query.get(education_id)
        if education:
            db.session.delete(education)
            db.session.commit()
            return education
        return None