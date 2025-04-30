import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Định nghĩa model path
MODEL_PATH = "./models/liver-histopathology-fibrosis-ultrasound-model.keras"

try:
    model = load_model(MODEL_PATH)
    print("\n✅ Model loaded successfully!")
except Exception as e:
    print(f"\n❌ Error loading model: {str(e)}")
    model = None

def preprocess_image(img_path):
    """ Tiền xử lý ảnh trước khi đưa vào mô hình """
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0) 
        return img_array
    except Exception as e:
        print(f"\n❌ Error processing image: {str(e)}")
        return None

def predict_liver_disease(img_path):
    """ Hàm dự đoán bệnh gan dựa trên ảnh """
    if model is None:
        return "Model chưa được tải!"

    img_array = preprocess_image(img_path)
    if img_array is None:
        return "Lỗi xử lý ảnh!"

    prediction = model.predict(img_array)

    if prediction.shape[1] == 1: 
        predicted_label = "Có bệnh" if prediction[0][0] > 0.5 else "Không có bệnh"
    else: 
        predicted_label = int(np.argmax(prediction))  

    return predicted_label
