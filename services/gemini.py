import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from your .env file.")

# Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Current model
MODEL = "gemini-3.5-flash"


# ============================================================
# LIFESTYLE ANALYSIS
# ============================================================

def analyze_lifestyle(lifestyle):

    prompt = f"""
You are EcoPath AI, an environmental lifestyle assistant.

Analyze the user's lifestyle and explain their environmental impact.

USER LIFESTYLE:
{lifestyle}

Return the response using EXACTLY these sections:

CARBON FOOTPRINT
Give a rating from:
Very Low
Low
Moderate
High
Very High

Then give a short explanation.


MAIN ENVIRONMENTAL IMPACTS
Explain the user's biggest environmental impacts based only on
the information they provided.


RECOMMENDATIONS
Give exactly 5 practical recommendations specifically based
on their answers.


CONCLUSION
Give a short encouraging conclusion.

IMPORTANT:
- Return only HTML. Do not use Markdown.
- Do not use ###.
- Do not use **.
- Do not use emojis.
- Keep the language simple and clear.
- Do not invent information.
- Make each section easy to read.
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text

    except Exception as e:

        return (
            "Unable to generate your EcoPath analysis right now.\n\n"
            f"Error: {str(e)}"
        )


# ============================================================
# GEMINI CHAT
# ============================================================

chat_history = []


def chat(message):

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=message
        )

        return response.text

    except Exception as e:

        return f"Sorry, I couldn't respond right now. Error: {str(e)}"


def reset_chat():

    global chat_history

    chat_history = []

    return True