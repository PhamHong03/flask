from flask import jsonify, request
from database import db
from models.account import Account

def register_account(data): 
    if Account.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email đã được sử dụng"}), 400

    # hashed_password = Account.hash_password(data['password'])

    new_account = Account(
        email=data['email'],
        password=data['password'], 
        role=data['role']
    )

    db.session.add(new_account)
    db.session.commit()

    return jsonify({
        "message": "Tạo tài khoản thành công",
        "id": new_account.id, 
        "email": new_account.email,
        "role": new_account.role
    }), 201
def login_account():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Thiếu email hoặc mật khẩu"}), 400

    email = data.get('email')
    input_password = data.get('password')


    account = Account.query.filter_by(email=email).first()
    print(account)
    if not account:
        return jsonify({"message": "Tài khoản không tồn tại"}), 404

    # Kiểm tra mật khẩu
    if not Account.check_password(account.password, input_password):
        return jsonify({"message": "Mật khẩu không đúng"}), 400

    return jsonify({
        "message": "Đăng nhập thành công",
        "account": {
            "id": account.id,
            "email": account.email,
            "role": account.role
        }
    }), 200

def get_all_accounts():
    """Lấy danh sách tất cả tài khoản"""
    accounts = Account.query.all()
    return jsonify([{
        "id": acc.id,
        "email": acc.email,
        "role": acc.role
    } for acc in accounts]), 200
