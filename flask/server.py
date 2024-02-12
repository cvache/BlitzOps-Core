#!/usr/bin/env python
import os

from flask import Flask, request
from models import CheckpointPostRequest
from pydantic import ValidationError
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")

@app.route('/')
def v1():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!----\n"

@app.route('/checkpoint', methods=['POST'])
def checkpoint():

    #get data from request
    resp = request.get_json()
    
    # Validate data
    try:
        cpr = CheckpointPostRequest(**resp)
    except ValidationError as e:
        return("Could not validate payload. Ensure it is formatted correctly")
    
    #Setup database connection
    try:
        client = MongoClient("mongodb://0.0.0.0:27017/")
        db = client.BlitzOps
        checkpoints = db.checkpoints
    except Exception as e:
        return("Could not connect to database")

    # Insert into database
    try:
        db_resp = checkpoints.insert_one(cpr.model_dump())
    except Exception as e:
        return("Could not insert into database")
    
    return db_resp.inserted_id


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
    