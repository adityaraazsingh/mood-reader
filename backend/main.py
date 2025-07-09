from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
import re

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "https://mood-reader-rho.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Hugging Face API token
HF_API_TOKEN = os.getenv("HF_API_TOKEN")  # Make sure this is set in your environment or .env file

# ---------------- Model -------------------
class EmotionRequest(BaseModel):
    text: str

# ---------------- Emotion Metadata -------------------
emotion_metadata = {
    "joy": {
        "emoji": "😊",
        "color": "#FFD54F",
        "tone": "Positive",
        "suggestion": "Enjoy the moment and spread the joy!",
        "response": "I'm glad you're feeling happy!"
    },
    "sadness": {
        "emoji": "😢",
        "color": "#1E8BFF",
        "tone": "Negative",
        "suggestion": "It’s okay to feel sad. Talk to someone you trust.",
        "response": "I’m here for you if you need to talk."
    },
    "anger": {
        "emoji": "😠",
        "color": "#F85B58",
        "tone": "Negative",
        "suggestion": "Try taking a few deep breaths to calm down.",
        "response": "That sounds frustrating. I'm here to listen."
    },
    "fear": {
        "emoji": "😨",
        "color": "#9A79FF",
        "tone": "Negative",
        "suggestion": "Try grounding yourself and focusing on the present.",
        "response": "It’s normal to be scared sometimes."
    },
    "surprise": {
        "emoji": "😲",
        "color": "#CCFD5A",
        "tone": "Neutral",
        "suggestion": "Unexpected things can be exciting or scary—take a moment to reflect.",
        "response": "Whoa, that’s surprising!"
    },
    "love": {
        "emoji": "❤️",
        "color": "#FF79A6",
        "tone": "Positive",
        "suggestion": "Love makes life beautiful. Let it flow.",
        "response": "That’s so heartwarming to hear!"
    },
    "neutral": {
        "emoji": "😐",
        "color": "#FEFFFD",
        "tone": "Neutral",
        "suggestion": "Keep observing your feelings and environment.",
        "response": "Got it. Just a regular moment, huh?"
    }
}

# ---------------- Utility Functions -------------------
def extract_keywords(text):
    words = re.findall(r'\b\w{5,}\b', text.lower())
    return list(set(words))[:5]

def classify_intensity(score):
    if score > 0.85:
        return "High"
    elif score > 0.6:
        return "Moderate"
    else:
        return "Low"

# ---------------- Route -------------------
@app.post("/analyze")
async def analyze_emotion(request: EmotionRequest):
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
            headers=headers,
            json={"inputs": request.text}
        )

    data = response.json()

    # Handle errors gracefully
    if isinstance(data, dict) and data.get("error"):
        return {"error": data["error"]}

    result = data[0][0]
    label = result["label"].lower()
    score = result["score"]

    meta = emotion_metadata.get(label, emotion_metadata["neutral"])

    return {
        "emotion": label.capitalize(),
        "confidence": f"{round(score * 100, 2)}%",
        "emoji": meta["emoji"],
        "tone": meta["tone"],
        "summary": f"You seem to be feeling {label}.",
        "intensity": classify_intensity(score),
        "keywords": extract_keywords(request.text),
        "color_code": meta["color"],
        "suggestion": meta["suggestion"],
        "response_text": meta["response"]
    }

#  python -m uvicorn main:app --reload