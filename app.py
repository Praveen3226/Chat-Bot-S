from flask import Flask, request, jsonify, render_template 
import requests
import os
from difflib import get_close_matches



app = Flask(__name__)

API_KEY = "AIzaSyCiMT35cysNSXz9HqCmcmgG3fGSXfuk3Yw"  # Keep your key safe!
GEMINI_MODEL = "models/gemini-2.0-flash:generateContent"

@app.route("/")
def index():
    return render_template("index.html")


CANNED_RESPONSES = {
    "cart abandonment": "We help recover carts using AI that detects drop-off points and sends smart reminders.",
    "lead follow-up": "We automate lead nurturing using personalized email/SMS drip sequences.",
    "customer support": "Our AI chatbot offers 24/7 help, answers questions, and escalates to a human if needed.",
    "ads": "We optimize your ad spend by analyzing your campaign data and adjusting in real time."
}

def get_matching_canned_response(user_query):
    keywords = list(CANNED_RESPONSES.keys())
    match = get_close_matches(user_query.lower(), keywords, n=1, cutoff=0.4)
    if match:
        return CANNED_RESPONSES[match[0]]
    return None


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_text = data.get("message", "").strip()

    if not user_text:
        return jsonify({"error": "Message cannot be empty."}), 400

    url = f"https://generativelanguage.googleapis.com/v1beta/{GEMINI_MODEL}"

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    canned = get_matching_canned_response(user_text)

    prompt_text = f"""
You are Solivox Assistant, an expert in e-commerce automation and AI SaaS tools.
Solivox AI builds AI-powered tools for: cart recovery, AI chatbots, lead follow-up, and ad optimization.
If a short predefined response exists for the query, elaborate and tailor it to the user’s context.
Be concise, solution-oriented, and sound like a helpful co-founder.

User Question: {user_text}
Short Answer (if any): {canned or "None"}
    """

    # ✅ Use prompt_text here
    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt_text
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        print("Response status:", response.status_code)
        print("Response content:", response.text)
        response.raise_for_status()
        resp_json = response.json()

        reply_text = resp_json["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"response": reply_text})

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error:", http_err)
        print("Response text on error:", response.text)
        return jsonify({"error": f"HTTP error: {http_err}"}), response.status_code
    except Exception as e:
        print("Unexpected error:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
