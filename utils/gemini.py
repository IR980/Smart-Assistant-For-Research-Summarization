import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "AIzaSyD9sd6Jpwx0PgTPWk4M3NBbhR-ryXtfic4"

def gemini_chat(prompt: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY,
    }
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    try:
        res = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        res.raise_for_status()
        text = res.json()['candidates'][0]['content']['parts'][0]['text']
        return json.loads(text) if text.strip().startswith("{") else {"feedback": text}
    except Exception as e:
        return {"feedback": "Gemini error", "justification": str(e)}

gemini_call = gemini_chat

def call_gemini(prompt: str):
    """
    Sends a prompt to Google Gemini API and returns the generated content as plain text.
    """
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "Error: Could not connect to Gemini."


import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"


# utils/gemini.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

HEADERS = {
    "Content-Type": "application/json"
}

def call_gemini(prompt):
    body = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_URL, headers=HEADERS, json=body)
        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"❌ Error answering question: {e}"
