from pydantic import BaseModel

class CheckpointPostRequest(BaseModel):
    workflow_id: str
    run_id: str
    checkpoint_id: str
    timestamp: float

class CheckpointGetRequest(BaseModel):
    workflow_id: str
    run_id: str | None = None
