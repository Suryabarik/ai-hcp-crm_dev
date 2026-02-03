from services.ai_service import analyze_interaction_with_groq

class SummarizerAgent:
    """
    AI agent responsible for summarizing HCP interactions
    using Groq LLM (gemma2-9b-it).
    """

    def summarize(self, raw_text: str):
        """
        Sends raw interaction text to Groq and returns structured analysis.
        """
        return analyze_interaction_with_groq(raw_text)
