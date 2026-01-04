# AI Chatbot – Chat with Einstein 🤖🧠

![Python](https://img.shields.io/badge/Python-3.12-blue)
![LangChain](https://img.shields.io/badge/LangChain-LLM-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini-green)
![Gradio](https://img.shields.io/badge/UI-Gradio-red)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered chatbot that simulates conversations with **Albert Einstein**, built using **Google Gemini**, **LangChain**, and **Gradio**.  
This project showcases practical implementation of Large Language Models (LLMs) with memory and an interactive web-based UI.

---

## 📌 Project Overview

The AI Chatbot enables users to interact with an AI persona inspired by Albert Einstein.  
It integrates an LLM with conversational memory and a lightweight UI to create a realistic and engaging chat experience.

This project is suitable for:
- AI/ML portfolios
- Learning LangChain workflows
- Demonstrating real-world LLM integration

---

## 🚀 Features

- Persona-based chatbot (Albert Einstein)
- Powered by **Google Gemini (Flash / Lite)**
- Conversation memory using **LangChain**
- Web-based UI with **Gradio**
- Secure API key management using environment variables
- Easy local setup and execution

---

## 🛠️ Tech Stack

| Category | Technology |
|--------|------------|
| Language | Python 3.12 |
| LLM | Google Gemini |
| Framework | LangChain |
| UI | Gradio |
| Config | python-dotenv |

---

## 📂 Project Structure

```text
AI_Chatbot/
├── main.py          # Core chatbot logic and UI
├── einstein.png     # Chatbot avatar
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ⚙️ Installation & Setup

git clone https://github.com/Rohit-more-2003/AI_Chatbot.git<br>
cd AI_Chatbot

python -m venv venv <br>
source venv/bin/activate      # Linux / macOS<br>
venv\Scripts\activate         # Windows<br>

pip install -r requirements.txt

---

## 🔑 Environment Variables

GOOGLE_API_KEY=your_gemini_api_key_here

---

## ▶️ Run the Application

python main.py
