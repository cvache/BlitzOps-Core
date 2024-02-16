from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import pymongo
import motor.motor_asyncio

from .models import (
    CheckpointPostRequest, CheckpointGetRequest
)

@asynccontextmanager
async def lifespan(app:FastAPI):
    #Startup
    MONGO_CLIENT = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017/")
    MONGO_DB = MONGO_CLIENT.BlitzOps
    MONGO_COLLECTION = MONGO_DB.checkpoints

    app.state.MONGO_COLLECTION = MONGO_COLLECTION
    yield
        
app = FastAPI(lifespan=lifespan)
@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.post("/checkpoint")
async def add_checkpint(checkpoint: CheckpointPostRequest, request: Request):    

    # Insert into database
    try:
        db_resp = await request.app.state.MONGO_COLLECTION.insert_one(checkpoint.model_dump())
    except Exception as e:
        print("Error inserting into database")
        return(str(e))
    
    return str(db_resp.inserted_id)

@app.get("/get_flow")
async def get_flow(request_data:CheckpointGetRequest, request: Request):
    query ={
        "workflow_id": request_data.workflow_id
    }
    if request_data.run_id:
        query["run_id"] = request_data.run_id

    cursor = request.app.state.MONGO_COLLECTION.find(query, {"_id": 0})
    results = []
    async for doc in cursor:
        results.append(doc)

    return str(results)
