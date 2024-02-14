from pydantic_core import ValidationError
from pydantic import BaseModel
import uuid

from pymongo import MongoClient

class CheckpointPostRequest(BaseModel):
    workflow_id: str
    run_id: str
    checkpoint_id: str
    timestamp: float

payload = {
        "workflow_id": "wf1",
        "run_id": str(uuid.uuid4()),
        "checkpoint_id": "123",
        "timestamp": 123.123
}

def validate():

    try:
        cpr = CheckpointPostRequest(**payload)
    except ValidationError as e:
        print(e)
        print("BEEP")
    
    print(cpr.workflow_id)


def db():
    resp = payload
    
    # Validate data
    try:
        cpr = CheckpointPostRequest(**resp)
    except ValidationError as e:
        return("Could not validate payload. Ensure it is formatted correctly")
    
    #Setup database connection
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client.BlitzOps
        checkpoints = db.checkpoints
    except Exception as e:
        return("Could not connect to database")

    # Insert into database
    try:
        db_resp = checkpoints.insert_one(cpr.model_dump())
    except Exception as e:
        return(str(e))
    
    return db_resp.inserted_id
 

if __name__ == "__main__":
    db()
    