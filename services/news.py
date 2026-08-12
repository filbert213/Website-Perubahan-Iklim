import os
import requests


def get_article_category(article):
    """
    Automatically categorize an environmental news article.
    """

    text = (
        (article.get("title") or "") + " " +
        (article.get("description") or "")
    ).lower()

    # Climate
    if any(word in text for word in [
        "climate",
        "global warming",
        "heatwave",
        "heat wave",
        "temperature",
        "carbon",
        "emission",
        "greenhouse gas"
    ]):
        return "🌍 Climate"

    # Nature
    if any(word in text for word in [
        "wildlife",
        "forest",
        "biodiversity",
        "species",
        "conservation",
        "deforestation",
        "habitat"
    ]):
        return "🌿 Nature"

    # Pollution
    if any(word in text for word in [
        "plastic",
        "pollution",
        "waste",
        "recycling",
        "contamination",
        "landfill",
        "microplastic"
    ]):
        return "♻️ Pollution"

    # Clean Energy
    if any(word in text for word in [
        "solar",
        "wind power",
        "renewable energy",
        "renewable",
        "electric vehicle",
        "electric vehicles",
        "battery",
        "clean energy",
        "hydrogen"
    ]):
        return "⚡ Clean Energy"

    # Technology
    if any(word in text for word in [
        "innovation",
        "technology",
        "invention",
        "green technology",
        "eco technology",
        "new technology",
        "electric",
        "device"
    ]):
        return "💡 Technology"

    # Oceans
    if any(word in text for word in [
        "ocean",
        "marine",
        "coral",
        "sea",
        "coastal",
        "fishing"
    ]):
        return "🌊 Oceans"

    # Sustainability
    if any(word in text for word in [
        "sustainability",
        "sustainable",
        "eco-friendly",
        "green living",
        "circular economy"
    ]):
        return "🌱 Sustainability"

    # Default
    return "🌎 Environment"


def get_climate_news():

    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("ERROR: NEWS_API_KEY is not set.")
        return []

    url = "https://newsapi.org/v2/everything"

    query = (
        '"climate change" OR '
        '"global warming" OR '
        'pollution OR '
        'sustainability OR '
        '"renewable energy" OR '
        'conservation OR '
        'biodiversity OR '
        '"clean energy" OR '
        '"plastic pollution" OR '
        'deforestation OR '
        '"environmental protection" OR '
        'wildlife OR '
        'ocean OR '
        '"green technology"'
    )

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 12,
        "apiKey": api_key
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        print("NewsAPI status:", response.status_code)

        if response.status_code != 200:
            print("NewsAPI error:", response.text)
            return []

        data = response.json()

        articles = data.get("articles", [])

        # Remove invalid articles
        articles = [
            article for article in articles
            if article.get("title")
            and article.get("title") != "[Removed]"
        ]

    except requests.RequestException as error:

        print("NewsAPI connection error:", error)
        return []

    except Exception as error:

        print("Unexpected news error:", error)
        return []

    # Categorize articles AFTER the try/except
    for article in articles:
        article["category"] = get_article_category(article)

    return articles