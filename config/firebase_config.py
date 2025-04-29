import firebase_admin
from firebase_admin import credentials, auth

#Load Firebase Admin SDK
cred = credentials.Certificate("diagnose-app-aa9c8-firebase-adminsdk-fbsvc-7ca27fa1fc.json")
firebase_admin.initialize_app(cred)
