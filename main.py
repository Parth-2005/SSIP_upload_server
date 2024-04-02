from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json
from flask import Flask, jsonify

mongo = MongoClient("mongodb+srv://23bit009:uTIJOIdpKFXOn8PL@cluster0.eltoend.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = mongo['weatherdb']
cities = db.cities

app = Flask(__name__)

@app.route('/search/<data>', methods=['POST'])
def search(data):
    #search with regex expression
    result = cities.find({"name": {"$regex": f".*{data}.*", "$options": "i"}}).limit(5)
    return jsonify(list(result))

if __name__ == '__main__':
    app.run()
