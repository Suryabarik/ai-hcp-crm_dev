'''
from fastapi import APIRouter, Depends
from typing import List

from schemas.interaction_schema import InteractionCreate, InteractionResponse
from services.interaction_service import (
    log_interaction_service,
    edit_interaction_service,
    get_interactions_service
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)

@router.post("/log", response_model=InteractionResponse)
def log_interaction(data: InteractionCreate):
    """
    Log a new HCP interaction using LangGraph + Groq
    """
    return log_interaction_service(data)


@router.put("/edit/{interaction_id}", response_model=InteractionResponse)
def edit_interaction(interaction_id: int, data: InteractionCreate):
    """
    Edit an existing interaction
    """
    return edit_interaction_service(interaction_id, data)


@router.get("/", response_model=List[InteractionResponse])
def get_all_interactions():
    """
    Fetch all logged interactions
    """
    return get_interactions_service()
'''
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.interaction_schema import InteractionCreate, InteractionResponse
from services.interaction_service import (
    log_interaction_service,
    edit_interaction_service,
    get_interactions_service
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)

@router.post("/log", response_model=InteractionResponse)
def log_interaction(
    data: InteractionCreate,
    db: Session = Depends(get_db)   # ✅ THIS WAS MISSING
):
    return log_interaction_service(db=db, data=data)  # ✅ FIXED


@router.put("/edit/{interaction_id}", response_model=InteractionResponse)
def edit_interaction(
    interaction_id: int,
    data: InteractionCreate,
    db: Session = Depends(get_db)
):
    return edit_interaction_service(db=db, interaction_id=interaction_id, data=data)


@router.get("/", response_model=List[InteractionResponse])
def get_all_interactions(db: Session = Depends(get_db)):
    return get_interactions_service(db=db)
