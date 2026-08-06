from flask import Flask, render_template, request
from services.gemini import analyze_lifestyle

app = Flask(__name__)

# ----
# HOME
# ----

@app.route("/")
def home():
    return render_template("index.html")


# ----
# NEWS
# ----

@app.route("/news")
def news():

    # Placeholder data
    articles = [

        {
            "title":"Renewable Energy Continues to Expand",
            "description":"Countries are investing heavily in renewable energy to reduce emissions.",
            "image":"https://images.unsplash.com/photo-1473448912268-2022ce9509d8?w=800",
            "category":"Energy",
            "date":"Today",
            "url":"#"
        },

        {
            "title":"Ocean Temperatures Reach Record High",
            "description":"Scientists warn that rising ocean temperatures affect marine ecosystems.",
            "image":"https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=800",
            "category":"Ocean",
            "date":"Yesterday",
            "url":"#"
        },

        {
            "title":"Cities Plant More Urban Forests",
            "description":"Urban greening projects improve air quality and reduce heat.",
            "image":"https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
            "category":"Forest",
            "date":"2 days ago",
            "url":"#"
        }

    ]

    return render_template(
        "news.html",
        articles=articles
    )


# -----------
# AI ANALYSIS
# -----------

@app.route("/analysis", methods=["GET","POST"])
def analysis():

    if request.method == "POST":

        transport = request.form.get("transport")
        distance = request.form.get("distance")
        ac = request.form.get("ac")
        computer = request.form.get("computer")
        diet = request.form.get("diet")
        plastic = request.form.get("plastic")
        water = request.form.get("water")

        user_data = {
            "transport":transport,
            "distance":distance,
            "ac":ac,
            "computer":computer,
            "diet":diet,
            "plastic":plastic,
            "water":water
        }

        ai = analyze_lifestyle(user_data)

        return render_template(

            "analysis.html",

            result=ai["recommendation"],

            score=ai["score"],

            impact=ai["impact"]

        )

    return render_template("analysis.html")


# -------
# PLANNER
# -------

@app.route("/planner")
def planner():

    tasks = [

        {
            "day":"Monday",
            "tasks":[
                "Bring a reusable bottle",
                "Walk for short trips",
                "Turn off unused lights"
            ]
        },

        {
            "day":"Wednesday",
            "tasks":[
                "Use public transportation",
                "Recycle plastic bottles",
                "Avoid plastic bags"
            ]
        },

        {
            "day":"Friday",
            "tasks":[
                "Eat one vegetarian meal",
                "Take a shorter shower",
                "Share one climate fact"
            ]
        }

    ]

    return render_template(
        "planner.html",
        tasks=tasks
    )


# -----
# ABOUT
# -----

@app.route("/about")
def about():
    return render_template("about.html")


# -----
# ERROR
# -----

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404


# ---
# RUN
# ---

if __name__ == "__main__":

    app.run(
        debug=True
    )