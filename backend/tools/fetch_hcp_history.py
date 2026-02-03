from models.interaction import Interaction

def fetch_hcp_history_tool(db, hcp_id: int):
    """
    LangGraph Tool: Fetch past interactions of an HCP.
    """
    return db.query(Interaction).filter(
        Interaction.hcp_id == hcp_id
    ).all()
