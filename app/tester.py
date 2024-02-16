from pydantic_core import ValidationError
from pydantic import BaseModel
import pymongo
import uuid
import asyncio

import motor.motor_asyncio

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

try:
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
    db = client.BlitzOps
    checkpoints = db.checkpoints
except Exception as e:
    print(str(e))

def validate():

    try:
        cpr = CheckpointPostRequest(**payload)
    except ValidationError as e:
        print(e)
        print("BEEP")
    
    print(cpr.workflow_id)


async def db():
    resp = payload
    
    # Validate data
    try:
        cpr = CheckpointPostRequest(**resp)
    except ValidationError as e:
        return("Could not validate payload. Ensure it is formatted correctly")
    
    #Setup database connection
    

    # Insert into database
    try:
        db_resp = await checkpoints.insert_one(cpr.model_dump())
    except Exception as e:
        return(str(e))
    
    return db_resp.inserted_id

async def db_get(workflow_id:str, run_id:str=None):
    query ={
        "workflow_id": workflow_id
    }
    if run_id:
        query["run_id"] = run_id

    try:
        cursor = checkpoints.find(query).sort(
            "timestamp", pymongo.ASCENDING
        )
        results = []
        async for doc in cursor:
            del doc["_id"]
            results.append(doc)
        
        return results
    except Exception as e:
        return(str(e))
     

if __name__ == "__main__":
    v = asyncio.run(db()) 
    print(v) 

    # v = asyncio.run(db_get("wf1", "bestrun")) 
    # print(v)   