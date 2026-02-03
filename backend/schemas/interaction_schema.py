from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# -------- Request schema (log/edit interaction) --------
class InteractionCreate(BaseModel):
    hcp_id: int
    raw_text: str
    follow_up: Optional[str] = None

# -------- Response schema --------
class InteractionResponse(BaseModel):
    id: int
    hcp_id: int
    raw_text: str
    summary: Optional[str] = None
    sentiment: Optional[str] = None
    follow_up: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
