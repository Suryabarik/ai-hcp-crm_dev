from models.interaction import Interaction

def schedule_followup_tool(db, interaction_id: int, followup_date: str):
    """
    LangGraph Tool: Add or update follow-up date.
    """

    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return None

    interaction.follow_up = f"Follow-up scheduled on: {followup_date}"

    db.commit()
    db.refresh(interaction)

    return interaction
