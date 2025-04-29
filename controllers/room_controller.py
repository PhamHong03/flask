
from models.room import Room
from database import db

class RoomController:
    @staticmethod
    def get_rooms():
        return Room.query.all()
    
    @staticmethod
    def get_room_by_id(room_id):
        return Room.query.get(room_id)
    
    @staticmethod
    def create_room(data):
        new_room = Room(name=data['name'])
        db.session.add(new_room)
        db.session.commit()
        return new_room
    