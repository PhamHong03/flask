from flask import Blueprint, request, jsonify
from controllers.room_controller import RoomController

room_bp = Blueprint('room_bp', __name__)
@room_bp.route('/rooms', methods=['GET'])
def get_all_room():
    rooms = RoomController.get_rooms()

    if not rooms:
        return jsonify({"message": "Không có phòng"}), 404
    
    return jsonify([
        {
            "id" : room.id,
            "name" : room.name,
        }
        for room in rooms
    ]), 200

@room_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = RoomController.get_room(room_id)
    if not room:
        return jsonify({"message": "Không có phòng"}), 404
    return jsonify({
        "id" : room.id,
        "name" : room.name,
        }), 200
