from flask import Blueprint, request, jsonify
from controllers.account_controller import get_all_accounts, register_account, login_account

account_bp = Blueprint("account", __name__)

@account_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)

    if not data:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    return register_account(data)

@account_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"message": "Thiếu email hoặc mật khẩu"}), 400
    print(data)
    return login_account()

@account_bp.route("/accounts", methods=["GET"])
def get_accounts():
    return get_all_accounts()

@account_bp.route("/get_account_id", methods=["POST"])
def get_account_id():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"message": "Thiếu email"}), 400

    from database import db
    from models.account import Account

    user = db.session.query(Account).filter_by(email=email).first()
    if user:
        return jsonify({"id": user.id})  
    return jsonify({"message": "User not found"}), 404
