from flask import Flask, jsonify, request
from flask_cors import CORS 
import firebase_admin
import threading
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../recipesharingapplication-firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

initial_doc = ""

app = Flask(__name__)
CORS(app) 

@app.route('/add-document', methods=['POST'])
def add_document():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data"}), 400
        
        doc_ref = db.collection("users").add(data)
        
        return jsonify({"Success": True, "doc_id": doc_ref[1].id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/add", methods=["POST"], strict_slashes=False)
def add_message(message):
    doc_ref.set({"first": {message}, "last": "Lovelace", "born": 1815})

callback_done = threading.Event()

def on_snapshot(doc_snapshot, changes, read_time):
    global initial_doc
    for doc in doc_snapshot:
        print(f"Received document snapshot: {doc.id}")
        initial_doc = doc.to_dict().get("born", "No born Found")
    callback_done.set()

doc_watch = ""



@app.route('/get-document', methods=['GET'])
def get_document():
    global initial_doc, doc_watch
    try:
        doc_watch = doc_ref.on_snapshot(on_snapshot)
        callback_done.wait(timeout=5)
        return jsonify({"Success": True, "data": initial_doc}), 200
    except Exception as e:
        initial_doc = str(e)
        return jsonify({"Success": False, "error": str(e)}), 500

@app.route('/')
def home():
    get_document()
    return jsonify({"message": f"{initial_doc}"})

if __name__ == '__main__':
    app.run(debug=True)
