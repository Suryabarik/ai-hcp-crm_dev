from services.ai_service import analyze_interaction_with_groq

def sentiment_analyzer_tool(raw_text: str):
    """
    LangGraph Tool: Analyze sentiment using Groq.
    """

    ai_output = analyze_interaction_with_groq(raw_text)

    # Simple heuristic: just return raw AI output
    # (In real app you would parse JSON)
    return ai_output
