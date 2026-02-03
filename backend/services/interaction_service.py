'''
import json
from sqlalchemy.orm import Session
from models.hcp import HCP
from models.interaction import Interaction
from services.ai_service import analyze_interaction_with_groq

# -------- HCP SERVICES --------

def create_hcp_service(db: Session, data):
    hcp = HCP(
        name=data.name,
        hospital=data.hospital,
        specialty=data.specialty,
        city=data.city,
        phone=data.phone,
        email=data.email
    )
    db.add(hcp)
    db.commit()
    db.refresh(hcp)
    return hcp

def get_all_hcps_service(db: Session):
    return db.query(HCP).all()

# -------- INTERACTION SERVICES --------

def log_interaction_service(db: Session, data):
    # Call Groq to analyze text
    ai_output = analyze_interaction_with_groq(data.raw_text)

    # Convert AI response (string) to JSON
    try:
        parsed = json.loads(ai_output)
    except:
        # fallback if model gives messy output
        parsed = {
            "summary": ai_output,
            "sentiment": "neutral",
            "follow_up": data.follow_up
        }

    interaction = Interaction(
        hcp_id=data.hcp_id,
        raw_text=data.raw_text,
        summary=parsed.get("summary"),
        sentiment=parsed.get("sentiment"),
        follow_up=parsed.get("follow_up", data.follow_up)
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction

def edit_interaction_service(db: Session, interaction_id: int, data):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return None

    # Re-run AI analysis if raw text changed
    ai_output = analyze_interaction_with_groq(data.raw_text)

    try:
        parsed = json.loads(ai_output)
    except:
        parsed = {
            "summary": ai_output,
            "sentiment": "neutral",
            "follow_up": data.follow_up
        }

    interaction.raw_text = data.raw_text
    interaction.summary = parsed.get("summary")
    interaction.sentiment = parsed.get("sentiment")
    interaction.follow_up = parsed.get("follow_up", data.follow_up)

    db.commit()
    db.refresh(interaction)
    return interaction

def get_interactions_service(db: Session):
    return db.query(Interaction).all()

def get_hcp_history_service(db: Session, hcp_id: int):
    return db.query(Interaction).filter(
        Interaction.hcp_id == hcp_id
    ).all()
'''
import json
from sqlalchemy.orm import Session
from models.hcp import HCP
from models.interaction import Interaction
from services.ai_service import analyze_interaction_with_groq

# -------- HCP SERVICES --------

def create_hcp_service(db: Session, data):
    hcp = HCP(
        name=data.name,
        hospital=data.hospital,
        specialty=data.specialty,
        city=data.city,
        phone=data.phone,
        email=data.email
    )
    db.add(hcp)
    db.commit()
    db.refresh(hcp)
    return hcp

def get_all_hcps_service(db: Session):
    return db.query(HCP).all()

# -------- INTERACTION SERVICES --------
def log_interaction_service(db: Session, data):
    """
    Logs a new interaction with an HCP.
    Calls Groq API to analyze the interaction and stores the result.
    """

    # Call Groq AI service
    ai_output = analyze_interaction_with_groq(data.raw_text)

    # Handle ai_output being a dict (error) or a JSON string (success)
    if isinstance(ai_output, dict):
        # Groq API failed
        parsed = {
            "summary": "AI analysis failed: " + ai_output.get("error", "Unknown error"),
            "sentiment": "neutral",
            "follow_up": data.follow_up
        }
    else:
        # Try to parse JSON string
        try:
            parsed = json.loads(ai_output)
            if not isinstance(parsed, dict):
                parsed = {
                    "summary": str(parsed),
                    "sentiment": "neutral",
                    "follow_up": data.follow_up
                }
        except Exception:
            # Fallback if JSON parsing fails
            parsed = {
                "summary": str(ai_output),
                "sentiment": "neutral",
                "follow_up": data.follow_up
            }

    # Ensure summary is always a string
    summary_str = parsed.get("summary")
    if isinstance(summary_str, dict):
        summary_str = json.dumps(summary_str)  # convert dict to string

    # Create interaction object
    interaction = Interaction(
        hcp_id=data.hcp_id,
        raw_text=data.raw_text,
        summary=summary_str,
        sentiment=parsed.get("sentiment", "neutral"),
        follow_up=parsed.get("follow_up", data.follow_up)
    )

    # Save to DB
    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction



def edit_interaction_service(db: Session, interaction_id: int, data):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return None

    # Re-run AI analysis if raw text changed
    ai_output = analyze_interaction_with_groq(data.raw_text)

    try:
        parsed = json.loads(ai_output)
        if not isinstance(parsed, dict):
            parsed = {"summary": str(parsed), "sentiment": "neutral", "follow_up": data.follow_up}
    except:
        parsed = {
            "summary": str(ai_output),
            "sentiment": "neutral",
            "follow_up": data.follow_up
        }

    #summary_str = parsed.get("summary")
    #if isinstance(summary_str, dict):
    #    summary_str = json.dumps(summary_str)

    summary_str = parsed.get("summary")
    if isinstance(summary_str, dict):
       summary_str = "AI analysis failed: " + summary_str.get("error", "Unknown error")
    

    interaction.raw_text = data.raw_text
    interaction.summary = summary_str
    interaction.sentiment = parsed.get("sentiment", "neutral")
    interaction.follow_up = parsed.get("follow_up", data.follow_up)

    db.commit()
    db.refresh(interaction)
    return interaction

def get_interactions_service(db: Session):
    return db.query(Interaction).all()

def get_hcp_history_service(db: Session, hcp_id: int):
    return db.query(Interaction).filter(
        Interaction.hcp_id == hcp_id
    ).all()
