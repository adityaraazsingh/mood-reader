from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
import re

# ---------------- Setup -------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load emotion model
emotion_pipeline = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion", top_k=1)

# ---------------- Model -------------------
class EmotionRequest(BaseModel):
    text: str

# ---------------- Emotion Metadata Map -------------------
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
    return list(set(words))[:5]  # return top 5 unique long words

def classify_intensity(score):
    if score > 0.85:
        return "High"
    elif score > 0.6:
        return "Moderate"
    else:
        return "Low"

# ---------------- Route -------------------
@app.post("/analyze")
def analyze_emotion(request: EmotionRequest):
    result = emotion_pipeline(request.text)[0][0]
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