from business import party

from flask import Flask, request, jsonify
import pymongo
import settings


app = Flask(__name__)
client = pymongo.MongoClient(settings.MONGO_URI)
db = client.oiwai


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/parties', methods=['POST'])
def new_party():
    name = request.form['name']
    description = request.form['description']
    result, errors = party.create_party(db, name, description)
    if result:
        return jsonify('OK')
    else:
        return jsonify(errors)
