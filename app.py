from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate 
from config.config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import Account, Specialization, Education, Room, Physician
from routes.specialization_route import specialization_bp
from routes.education_route import education_bp
from routes.account_route import account_bp
# from routes.category_disease_route import category_disease_bp
# from routes.diagnose_disease_route import diagnose_disease_bp
from routes.physician_route import physician_bp
# from routes.patient_route import patient_bp 
from routes.room_route import room_bp
# from routes.medical_history_route import medical_history_bp
# from routes.application_form_route import application_form_bp
# from routes.appointment_form_route import appointment_form_bp
# from routes.upload_images_route import upload_images_bp
# from AI import ai_process_bp

from database import db
import pyrebase
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import pytz

vietnam_tz = pytz.timezone('Asia/Ho_Chi_Minh')

vietnam_time = datetime.now(vietnam_tz)
print("🕰 Server Time (Vietnam):", vietnam_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print("🇻🇳 Vietnam Time:", vietnam_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
bcrypt = Bcrypt(app)

# # 🔹 Định nghĩa thư mục lưu ảnh
# UPLOAD_FOLDER = 'uploads'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# Cấu hình Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/app_diagnose'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(specialization_bp)
app.register_blueprint(education_bp)
app.register_blueprint(account_bp)
# app.register_blueprint(category_disease_bp)
# app.register_blueprint(diagnose_disease_bp)
app.register_blueprint(physician_bp)
# app.register_blueprint(patient_bp)
app.register_blueprint(room_bp)
# app.register_blueprint(medical_history_bp)
# app.register_blueprint(application_form_bp)
# app.register_blueprint(appointment_form_bp)
# app.register_blueprint(upload_images_bp)

if __name__ == "__main__":
    # os.makedirs("uploads", exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
