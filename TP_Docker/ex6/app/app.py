from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_HOST = os.environ.get("MONGO_HOST", "db")
MONGO_PORT = os.environ.get("MONGO_PORT", "27017")

client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/",
                     serverSelectionTimeoutMS=5000)
db = client["tpdocker"]

@app.route("/")
def home():
    return "Hello from Flask + MongoDB inside Docker!\n"

@app.route("/db-check")
def db_check():
    try:
        client.admin.command("ping")
        db.visits.insert_one({"message": "connexion OK"})
        nb = db.visits.count_documents({})
        return f"Connexion MongoDB OK ({MONGO_HOST}:{MONGO_PORT}) - {nb} document(s) dans 'visits'\n"
    except Exception as e:
        return f"ECHEC connexion MongoDB : {e}\n", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
