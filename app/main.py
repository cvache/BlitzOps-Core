from fastapi import FastAPI
from pydantic import BaseModel

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
def add_checkpint(checkpoint: CheckpointPostRequest):
    return checkpoint.checkpoint_id