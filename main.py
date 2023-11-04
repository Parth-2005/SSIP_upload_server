from flask import Flask, request, jsonify
from flask_pymongo import MongoClient
from pymongo.server_api import ServerApi
from getmac import get_mac_address
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SECRET_KEY"]="SECRET"
mongo = MongoClient("mongodb+srv://nasaapplication:password123parthandnasaapplication@cluster0.kq6h2lm.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

mongo = mongo["SSIP"]
Students = mongo.students


@app.route('/insertData', methods=['POST'])
def insert_data():
    print("Hello")
    try:
        # Get data from the request
        data = request.get_json()

        # Ensure 'roll' and 'MAC' are present in the request data
        if 'roll' not in data:
            return jsonify({'error': 'Roll and MAC are required'}), 400

        # Insert data into MongoDB
        Students.find_one_and_update({"roll": data["roll"]}, {'$set': {"mac" : get_mac_address(ip=request.remote_addr)}})

        return jsonify({'message': 'Data inserted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")