from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = pymongo.MongoClient(MONGO_URL)
db = client.nandish
collection = db['test']

app = Flask(__name__)
@app.route('/')
def home():
    return 'Backend hiii'
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    collection.insert_one(form_data)
    return 'Data submitted!'

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for i in data:
        del i['_id']
    return {'Data': data}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
