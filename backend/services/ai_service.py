from groq import Groq, GroqError
import os

API_KEY = os.getenv("GROQ_API_KEY")
# ✅ Hardcoded API key (for instant testing)


# Initialize Groq client
client = Groq(api_key=API_KEY)

def analyze_interaction_with_groq(raw_text: str):
    """
    Sends user text to Groq and returns structured analysis
    """
    prompt = f"""
    Analyze the following HCP interaction and extract:
    - short summary (2-3 sentences)
    - sentiment (positive/neutral/negative)
    - suggested follow-up action

    Text:
    {raw_text}

    Respond in JSON format like:
    {{
      "summary": "...",
      "sentiment": "...",
      "follow_up": "..."
    }}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        # Return the content from Groq response
        return response.choices[0].message.content

    except GroqError as e:
        # Catch authentication or other errors and return a descriptive message
        return {
            "error": "Failed to call Groq API",
            "details": str(e)
        }
