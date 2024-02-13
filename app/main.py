from fastapi import FastAPI
from pydantic import BaseModel
import motor.motor_tornado

class CheckpointPostRequest(BaseModel):
    workflow_id: str
    run_id: str
    checkpoint_id: str
    timestamp: float

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.post("/checkpoint")
async def add_checkpint(checkpoint: CheckpointPostRequest):
    #Setup database connection
    try:
        client = motor.motor_tornado.MotorClient("mongodb://localhost:27017/")
        db = client.BlitzOps
        checkpoints = db.checkpoints
    except Exception as e:
        return("Could not connect to database")

    # Insert into database
    try:
        db_resp = await db.checkpoints.insert_one(checkpoint.model_dump())
    except Exception as e:
        return(str(e))
    
    return db_resp.inserted_id