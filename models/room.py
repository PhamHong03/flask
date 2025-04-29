from database import db

class Room(db.Model):
    __tablename__ = 'room' 

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # application_forms = db.relationship('ApplicationForm', back_populates='room', cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name