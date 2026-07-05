# Chat with Einstein 🤖🧠

An AI-powered chatbot that simulates conversations with **Albert Einstein** using **Google Gemini**, **LangChain**, and **Gradio**. The chatbot responds in Einstein's style by combining scientific explanations with personal anecdotes and a touch of humor.

---

## Features

- Conversational AI powered by Google Gemini
- Persona-based responses as Albert Einstein
- Maintains conversation history
- Simple and interactive Gradio web interface
- Clear Chat functionality
- Lightweight Python application

---

## Tech Stack

- Python 3.x
- Google Gemini API
- LangChain
- Gradio
- Python Dotenv

---

## Project Structure

```
.
├── main.py
├── requirements.txt
├── .env
├── einstein.png
├── README.md
└── Dockerfile (optional)
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

Replace `your_google_gemini_api_key` with your actual API key.

---

## Running the Application

Run:

```bash
python main.py
```

The Gradio interface will start, and a local URL will be displayed in the terminal.

Open the URL in your browser to start chatting with Einstein.

---

## Example Conversation

##### You

> Explain the theory of relativity.

##### Einstein

> Ah, relativity has been my lifelong companion! I remember spending years imagining what it would be like to ride alongside a beam of light. That simple thought experiment eventually led to ideas that changed physics. Fortunately, the equations are much easier to write than my hairstyle was to maintain!

---

## Requirements

Dependencies are listed in `requirements.txt`.

Main libraries used:

- gradio
- langchain
- langchain-google-genai
- python-dotenv
- google-genai

---

## Docker (Optional)

Build the Docker image:

```bash
docker build -t einstein-chatbot .
```

Run the container:

```bash
docker run -p 7860:7860 \
-e GEMINI_API_KEY=your_api_key \
einstein-chatbot
```

---

## Future Improvements

- Multiple historical personalities
- Streaming AI responses
- Voice input and output
- Chat history export
- Theme customization
- Conversation memory persistence

---

## Author

### Rohit More
