from flask import Flask, render_template, jsonify, request
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

load_dotenv()

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db["Todo Items"]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submittodoitem', methods=['POST'])
def submit():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return "Data submitted successfully"


if __name__ == '__main__':
    app.run(debug=True)