````markdown
# 🌈 Mood Reader – Emotion Reflection Tool

A simple full-stack web app that allows users to input short emotional reflections and get feedback on the detected emotion.

Built as part of an internship assignment, this app showcases frontend/backend integration using Angular and FastAPI. It leverages Hugging Face’s emotion classification model and returns enriched emotional insights including intensity, suggestions, and emojis.

---

## 📸 Live Demo

- **Frontend (Angular, deployed on Vercel):**  
  👉 [https://mood-reader-rho.vercel.app/](https://mood-reader-rho.vercel.app/)

- **Backend (FastAPI, deployed on Render):**  
  👉 [https://mood-reader-api.onrender.com/docs](https://mood-reader-api.onrender.com/docs)

---

## ✨ Features

- Emotion analysis using Hugging Face (`bert-base-go-emotion`)
- Sends JSON responses with:
  - `emotion` name
  - `confidence` percentage
  - `emoji` representation
  - `intensity` level
  - `suggestion` and `response_text`
- Clean UI with:
  - Mobile-first layout
  - Loading state while processing
  - Responsive, styled results

---

## 🧠 Tech Stack

### 🔹 Frontend
- **Angular** (TypeScript)
- Angular Material UI components
- Hosted on **Vercel**

### 🔹 Backend
- **FastAPI** (Python)
- Hugging Face Transformers via Inference API
- Hosted on **Render**

---

## 🧪 API Endpoint

### `POST /analyze`

**Request:**

```json
{
  "text": "I feel nervous about my first job interview"
}
````

**Response:**

```json
{
  "emotion": "Fear",
  "confidence": "84.65%",
  "emoji": "😨",
  "tone": "Negative",
  "summary": "You seem to be feeling fear.",
  "intensity": "Moderate",
  "keywords": ["nervous", "interview"],
  "color_code": "#9A79FF",
  "suggestion": "Try grounding yourself and focusing on the present.",
  "response_text": "It’s normal to be scared sometimes."
}
```

---

## 🚀 Running the Project Locally

### 🔧 Backend (FastAPI)

1. Navigate to the `backend/` folder.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Hugging Face API token:

   ```env
   HF_API_TOKEN=hf_YourTokenHere
   ```
4. Start the server:

   ```bash
   python -m uvicorn main:app --reload
   ```

API will be available at:
`http://localhost:8000/docs`

---

### 🖼️ Frontend (Angular)

1. Navigate to the `frontend/` folder.
2. Install dependencies:

   ```bash
   npm install
   ```
3. Start the dev server:

   ```bash
   ng serve
   ```

Frontend will be available at:
`http://localhost:4200`

---

## 💡 Acknowledgements

* 🤗 **[Hugging Face](https://huggingface.co/)** for the `bert-base-go-emotion` model and Inference API.
* 💬 **ChatGPT (OpenAI)** for assistance in designing, optimizing, and debugging the application.
* 📄 Assignment by Aman (Internship Team)

---

## 📁 Repository

This project is available at:
🔗 GitHub: https://github.com/adityaraazsingh/mood-reader/

---

## 🗓️ Submission Deadline

**12 July, 2025**

---

```

