import json
from models.interaction import Interaction
from services.ai_service import analyze_interaction_with_groq

def edit_interaction_tool(db, interaction_id: int, new_text: str, ai_output: str = None):
    """
    LangGraph Tool: Edit an existing interaction.
    """

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return None

    if not ai_output:
        ai_output = analyze_interaction_with_groq(new_text)

    try:
        parsed = json.loads(ai_output)
    except:
        parsed = {
            "summary": ai_output,
            "sentiment": "neutral",
            "follow_up": None
        }

    interaction.raw_text = new_text
    interaction.summary = parsed.get("summary")
    interaction.sentiment = parsed.get("sentiment")
    interaction.follow_up = parsed.get("follow_up")

    db.commit()
    db.refresh(interaction)

    return interaction
