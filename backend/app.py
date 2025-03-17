from flask import Flask, jsonify
from flask_cors import CORS 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("recipesharingapplication-firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

app = Flask(__name__)
CORS(app) 
@app.route('/')
def home():
    return jsonify({"message": "Recipe Sharing App Backend"})

if __name__ == '__main__':
    app.run(debug=True)
