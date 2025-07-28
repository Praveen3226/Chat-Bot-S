# 🤖 Solivox Assistant – AI-Powered E-commerce Automation Chatbot

Solivox Assistant is a lightweight Flask web application powered by Google Gemini API. It acts as a smart virtual co-founder that answers questions about Solivox AI’s e-commerce automation tools — such as cart recovery, lead follow-up, customer support, and ad optimization.

> 🎯 Designed for startups and solopreneurs who want instant guidance on AI-powered automation in e-commerce.

---

## 🚀 Features

- ✅ Predefined **canned responses** with smart matching using fuzzy keyword logic
- 🧠 **Google Gemini 2.0 Flash** integration for real-time AI-generated replies
- 🛍️ Context-aware prompt design for e-commerce automation use cases
- 🗣️ POST endpoint (`/chat`) for interactive chatbot responses
- 🖥️ Minimal front-end served via Flask (`index.html`)

---

## 💡 Type of Model and System
This is not a machine learning model itself, but rather an AI-enhanced chatbot application that combines:

## Rule-Based Logic (Canned Responses + Fuzzy Matching)
→ Uses string matching (like difflib.get_close_matches) to detect keywords and trigger predefined replies.
🔧 This is deterministic and rule-based.

## LLM API Integration (Google Gemini 2.0 Flash)
→ When canned responses don’t match, the system queries the Gemini 2.0 Flash model via API.
🧠 This brings natural language understanding and generation capabilities through Google’s generative model.

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Requests (for API calls)
- Google Gemini API (`v1beta`)
- HTML/Jinja2 for UI rendering

---

## 📦 Folder Structure

solivox-assistant/
│
├── app.py # Flask app with routes and Gemini integration
├── templates/
│ └── index.html # Basic front-end interface
├── static/ # Add CSS or JS if needed
└── README.md # You are here 🌟

---

## 🧪 Local Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/solivox-assistant.git
cd solivox-assistant
```bash

2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install flask requests

4. Run the app
python app.py
