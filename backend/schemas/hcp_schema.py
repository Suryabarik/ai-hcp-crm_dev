from pydantic import BaseModel, EmailStr
from typing import Optional

# -------- Request schema (when creating HCP) --------
class HCPCreate(BaseModel):
    name: str
    hospital: Optional[str] = None
    specialty: Optional[str] = None
    city: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None

# -------- Response schema (what API returns) --------
class HCPResponse(HCPCreate):
    id: int

    class Config:
        orm_mode = True
