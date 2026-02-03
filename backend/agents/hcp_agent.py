from agents.summarizer_agent import SummarizerAgent
from tools.log_interaction import log_interaction_tool
from tools.edit_interaction import edit_interaction_tool
from tools.fetch_hcp_history import fetch_hcp_history_tool
from tools.schedule_followup import schedule_followup_tool
from tools.sentiment_analyzer import sentiment_analyzer_tool

class HCPAgent:
    """
    Main AI agent that decides which tool to use
    for HCP interaction management.
    """

    def __init__(self):
        self.summarizer = SummarizerAgent()

    def process_interaction(self, raw_text: str, hcp_id: int, db):
        """
        1. Summarize using Groq
        2. Log interaction
        """
        ai_output = self.summarizer.summarize(raw_text)

        # Call tool to log interaction
        return log_interaction_tool(
            db=db,
            hcp_id=hcp_id,
            raw_text=raw_text,
            ai_output=ai_output
        )

    def edit_interaction(self, db, interaction_id: int, new_text: str):
        """
        Use AI to re-analyze and update an interaction.
        """
        ai_output = self.summarizer.summarize(new_text)

        return edit_interaction_tool(
            db=db,
            interaction_id=interaction_id,
            new_text=new_text,
            ai_output=ai_output
        )

    def get_hcp_history(self, db, hcp_id: int):
        """
        Fetch past interactions for an HCP.
        """
        return fetch_hcp_history_tool(db=db, hcp_id=hcp_id)

    def schedule_followup(self, db, interaction_id: int, date: str):
        """
        Schedule follow-up reminder.
        """
        return schedule_followup_tool(
            db=db,
            interaction_id=interaction_id,
            followup_date=date
        )

    def analyze_sentiment(self, raw_text: str):
        """
        Analyze sentiment of interaction.
        """
        return sentiment_analyzer_tool(raw_text)
