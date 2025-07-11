# 🧠 Offline Mental Wellness Companion  
*Privacy-First AI for Mental Health — Powered by Gemma 3n*

## ❗ Problem Statement  
Millions lack access to mental wellness tools due to internet, privacy, or device limitations. Current apps rely on cloud storage, online connectivity, and clinical frameworks that don't suit all users.

## 🚨 Real-World Gaps  
- Needs internet access  
- Stores sensitive data in the cloud  
- No offline AI support  
- Lacks regional language or voice  
- High resource consumption

## ✅ Our Solution  
An **offline, privacy-first mental wellness chatbot** running entirely on-device using a quantized **Gemma 3n 2B model** with:
- 📝 Journaling  
- 🌬️ Breathing Exercises  
- 🧠 Daily Check-ins  
- 🔒 Local-only data  
- 🌐 Multilingual support *(planned)*  
- 🔊 Offline voice support *(planned)*

## 🧠 Agent-Based Architecture  
- `JournalingAgent` – Empathetic reflection  
- `CheckInAgent` – Mood tracking  
- `BreathGuideAgent` – Calm routines  
- `ResponseAgent` – Gemma 3n LLM output  
- `FallbackAgent` – Non-clinical safety responses  
- `LanguageAdaptAgent` *(planned)*  
- `VoiceAgent` *(planned)*

## 📊 KPIs  
- Inference latency: < 2s  
- RAM: < 6 GB  
- Empathy rating: > 4.5/5  
- 100% offline capability

## ⚙️ Tech Stack  
- Gemma 3n 2B (GGUF)  
- `llama.cpp`  
- Python  
- Streamlit (optional UI)  
- Coqui TTS, Vosk (planned)

## ▶️ Run Locally  
1. Clone repo  
2. Install dependencies (`requirements.txt`)  
3. Run notebook: `mental_wellness_gemma.ipynb`  
4. (Optional) Run UI: `streamlit run app.py`

## 🔭 Future Scope  
- VoiceAgent for TTS/STT  
- BhāṣāGuru-style multilingual adaptation  
- Offline app export for Android

---
