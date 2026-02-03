"""
Reusable prompt templates for Groq (gemma2-9b-it).
All LLM prompts are centralized here so your system is clean and maintainable.
"""

LOG_INTERACTION_PROMPT = """
You are an AI assistant for a pharma CRM system.

Analyze the following HCP interaction text and extract structured information.

Text:
{raw_text}

Return ONLY valid JSON in this exact format (no explanation, no extra text):

{{
  "summary": "2-3 sentence concise summary",
  "sentiment": "positive or neutral or negative",
  "follow_up": "clear next action item"
}}
"""

EDIT_INTERACTION_PROMPT = """
You are updating an existing HCP interaction in a pharma CRM.

Re-analyze the revised text below and update the record accordingly.

Revised Text:
{raw_text}

Return ONLY valid JSON in this exact format:

{{
  "summary": "updated concise summary",
  "sentiment": "positive or neutral or negative",
  "follow_up": "updated next action"
}}
"""

SENTIMENT_ONLY_PROMPT = """
Classify the sentiment of this HCP interaction as:
positive, neutral, or negative.

Text:
{raw_text}

Return only one word: positive / neutral / negative
"""

HCP_HISTORY_SUMMARY_PROMPT = """
Summarize the interaction history of this HCP in 3-4 sentences
for a field representative before a new visit.

Interaction history:
{history_text}
"""

FOLLOWUP_REMINDER_PROMPT = """
Create a professional follow-up reminder message for a pharma sales rep.

Context:
{context}

Return a single short reminder sentence.
"""

def format_prompt(template: str, **kwargs) -> str:
    """
    Utility function to safely format prompts.
    Example:
      format_prompt(LOG_INTERACTION_PROMPT, raw_text="Met Dr. Rao today")
    """
    return template.format(**kwargs)
