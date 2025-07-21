# 🧠 AI Travel Assistant

**AI Travel Assistant** is a Python-based project that helps users plan trips using conversational AI. It answers travel-related queries, recommends destinations, and creates custom itineraries based on user input. The app runs locally and uses LangChain and Groq for fast, intelligent responses.

## ✨ Features

- 🌍 Travel question answering
- 🗺️ Destination suggestions
- 🧳 Itinerary planning
- 🧠 Conversational memory with LangChain
- ⚡ Fast inference via Groq LPU
- 🛡️ Environment-variable-based config

## 🛠️ Tech Stack

- Python 3.10+
- LangChain
- Groq SDK
- MCP (Modular Code Prompting)
- dotenv

## 🚀 Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Niyatilabala/AI_Travel_Assistant.git
```
```
cd AI_Travel_Assistant
```
### 2. Create Virtual Environment

```
python -m venv .venv
# Activate:
# On Windows
.venv\Scripts\activate
# On Mac/Linux
source .venv/bin/activate
#using uv
uv venv
```

### 3. Install Requirements

```
# using uv
uv add langchain-groq
uv add langchain-openai
uv add mcp-use
```

### 4. Configure Environment Variables

Copy the example ```.env``` file and add your own keys:

```
cp .env.example .env
```

Edit ```.env``` to include:

```
GROQ_API_KEY=your_key_here
OPENAI_API_KEY=your_openai_key_here
```
### 5. Run the App

```
python app.py
```

(Or python app.py if that’s your entry point.)

```
#using uv
uv run app.py
```

### 📁 Folder Structure

```
AI_Travel_Assistant/
├── .env
├── .env.example
├── .gitignore
├── app.py / main.py
├── mcp_use/
├── requirements.txt
└── README.md
```
```
#to create this repository using uv
uv init FILE_NAME
```
### ✅ Notes

Designed to run locally via CLI or script.

Keep your .env file secret — it's ignored by Git.

### 🧠 Credits

Groq

LangChain

MCP by Pietro Zullo
