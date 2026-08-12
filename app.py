from flask import Flask, render_template, request, jsonify

from services.gemini import chat, reset_chat
import os

from dotenv import load_dotenv

load_dotenv()

from services.news import get_climate_news
from services.gemini import analyze_lifestyle

app = Flask(__name__)


# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# CLIMATE NEWS
# =========================

@app.route("/news")
def news():
    articles = get_climate_news()

    return render_template(
        "news.html",
        articles=articles
    )


# =========================
# AI CHAT
# =========================

@app.route("/chat", methods=["POST"])
def chat_route():

    user_message = request.form.get("message", "").strip()

    if not user_message:
        return jsonify({
            "reply": "Please enter a message."
        })

    reply = chat(user_message)

    return jsonify({
        "reply": reply
    })


# =========================
# RESET CHAT
# =========================

@app.route("/reset-chat")
def reset():

    reset_chat()

    return jsonify({
        "success": True
    })


# =========================
# AI ANALYSIS
# =========================

@app.route("/analysis")
def analysis():

    return render_template(
        "analysis.html"
    )


# =========================
# LIFESTYLE PLANNER
# =========================

@app.route("/planner")
def planner():

    return render_template(
        "planner.html"
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )