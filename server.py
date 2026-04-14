from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = "AIzaSyAzXjYcO55GD356ScmbgfwPUWfTICqOUrA"

@app.route("/")
def home():
    return "Server running "

@app.route("/llm", methods=["POST"])
def llm():
    data = request.json
    user = data["user"]
    scheme = data["scheme"]

    prompt = f"""
User Profile:
Age: {user['age']}
Income: {user['income']}
Occupation: {user['occupation']}

Scheme:
{scheme['eligibility']}

Give JSON only:
{{
  "score": number (0 to 1),
  "reason": "short explanation"
}}
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    response = requests.post(
        url,
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )

    try:
        result = response.json()
        text = result["candidates"][0]["content"]["parts"][0]["text"]

        import json
        parsed = json.loads(text)

        return jsonify(parsed)

    except:
        return jsonify({"score": 0.5, "reason": "Gemini failed"})

if __name__ == "__main__":
    app.run(port=5000)