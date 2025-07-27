from flask import Flask,render_template,jsonify,request
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db["Tutorial database"]

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)

        # Basic validation to ensure no fields are empty
        if not all(form_data.values()):
            return render_template(
                "index.html",
                error="Please fill out all fields.",
                form_data=form_data
            )

        collection.insert_one(form_data)
        return "Data submitted successfully"
    except Exception as e:
        return render_template('index.html', error=str(e), form_data=request.form)

if __name__ == '__main__':
    app.run(debug=True)     