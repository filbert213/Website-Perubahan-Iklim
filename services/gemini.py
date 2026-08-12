import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are EcoPath AI.

You are a friendly AI sustainability assistant.

Your goals are:

• Help users understand climate change.
• Explain environmental topics in simple language.
• Give practical eco-friendly lifestyle advice.
• Create weekly sustainability plans.
• Help reduce carbon footprints.
• Recommend realistic actions for students.

Rules:

- Keep answers friendly.
- Keep answers concise unless the user asks for detail.
- Focus on climate, sustainability, recycling, renewable energy,
  transportation, food, electricity, and environmental education.
- If users ask unrelated questions, politely answer briefly and steer the
  conversation back toward sustainability when appropriate.
"""


class EcoPathChat:

    def __init__(self):

        self.chat = client.chats.create(
            model="gemini-2.5-flash",
            history=[
                {
                    "role": "user",
                    "parts": [{"text": SYSTEM_PROMPT}]
                },
                {
                    "role": "model",
                    "parts": [{"text": "Hello! I'm EcoPath AI. 🌱"}]
                }
            ]
        )

    def send(self, message):

        response = self.chat.send_message(message)

        return response.text

    def reset(self):

        self.__init__()


# Global chat instance
chatbot = EcoPathChat()


def chat(message):
    """
    Send a message to Gemini while keeping conversation history.
    """

    return chatbot.send(message)


def reset_chat():
    """
    Starts a new conversation.
    """

    chatbot.reset()


def analyze_lifestyle(data):

    prompt = f"""
Analyze the following lifestyle.

Transportation:
{data.get("transport")}

Electricity:
{data.get("electricity")}

Diet:
{data.get("diet")}

Recycling:
{data.get("recycling")}

Shopping:
{data.get("shopping")}

Return:

1. Carbon footprint level
2. Main impacts
3. Five recommendations
4. Encouraging conclusion
"""

    return chatbot.send(prompt)


def create_weekly_plan(goal):

    prompt = f"""
Create a detailed 7-day eco-friendly plan.

Goal:

{goal}
"""

    return chatbot.send(prompt)