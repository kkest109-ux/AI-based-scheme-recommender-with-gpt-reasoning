# AI Scheme Recommender

Browser based intelligent recommendation system using Sentence-BERT for semantic matching and a rule-based engine for eligibility checks (age, income, occupation). Integrates LLMs for explainable decisions and uses a hybrid scoring method. Built with Python and Streamlit for real-time, scalable performance.

## Files

- `ai_scheme_recommender.html` - Main HTML page with embedded styles and JavaScript.
- `updated_data.csv` - Scheme dataset used by the recommender.

## Run locally

1. Open a terminal in `c:\Users\hp\OneDrive\Desktop\genai`
2. Start a local HTTP server:

```powershell
python -m http.server 8000
```

3. Open the app in your browser:

```
http://127.0.0.1:8000/ai_scheme_recommender.html
```

## Notes

- The app loads `updated_data.csv` over HTTP, so it must be served from a web server rather than opened directly from the file system.
- The recommender uses local scoring heuristics for offline compatibility.
AIzaSyAzXjYcO55GD356ScmbgfwPUWfTICqOUrA
