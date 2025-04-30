
from database import db

class Diagnose_Disease(db.Model):
    
    __tablename__ = 'diagnose_disease'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diagnose_disease_name = db.Column(db.String(255), nullable=False)
    diagnose_disease_description = db.Column(db.Text, nullable=False)
    category_disease_id = db.Column(db.Integer, db.ForeignKey('category_disease.id'), nullable=False)
    
    category_disease = db.relationship('Category_Disease', back_populates="diagnose_diseases")
    # images = db.relationship('Images', back_populates='diagnose_disease', cascade="all, delete-orphan")

    def __init__(self, diagnose_disease_name, diagnose_disease_description, category_disease_id):
        self.diagnose_disease_name = diagnose_disease_name
        self.diagnose_disease_description = diagnose_disease_description
        self.category_disease_id = category_disease_id