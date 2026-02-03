from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from schemas.hcp_schema import HCPCreate, HCPResponse
from services.interaction_service import (
    create_hcp_service,
    get_all_hcps_service,
    get_hcp_history_service
)
from database.db import get_db  # Make sure you have a get_db dependency

router = APIRouter(
    prefix="/hcp",
    tags=["HCP"]
)

@router.post("/", response_model=HCPResponse)
def create_hcp(data: HCPCreate, db: Session = Depends(get_db)):
    """
    Create a new HCP profile
    """
    return create_hcp_service(db, data)


@router.get("/", response_model=List[HCPResponse])
def get_all_hcps(db: Session = Depends(get_db)):
    """
    Get list of all HCPs
    """
    return get_all_hcps_service(db)


@router.get("/{hcp_id}/history")
def get_hcp_history(hcp_id: int, db: Session = Depends(get_db)):
    """
    Get past interactions of a specific HCP
    """
    return get_hcp_history_service(db, hcp_id)
