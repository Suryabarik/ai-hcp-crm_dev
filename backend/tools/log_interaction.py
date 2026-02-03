import json
from models.interaction import Interaction
from services.ai_service import analyze_interaction_with_groq

def log_interaction_tool(db, hcp_id: int, raw_text: str, ai_output: str = None):
    """
    LangGraph Tool: Log a new HCP interaction.
    """

    # If AI output is not provided, call Groq
    if not ai_output:
        ai_output = analyze_interaction_with_groq(raw_text)

    try:
        parsed = json.loads(ai_output)
    except:
        parsed = {
            "summary": ai_output,
            "sentiment": "neutral",
            "follow_up": None
        }

    interaction = Interaction(
        hcp_id=hcp_id,
        raw_text=raw_text,
        summary=parsed.get("summary"),
        sentiment=parsed.get("sentiment"),
        follow_up=parsed.get("follow_up")
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction
