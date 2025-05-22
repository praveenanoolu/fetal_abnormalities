import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def ask_expert_llm(prompt: str):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "LLM API key not found. Please set GROQ_API_KEY environment variable."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a doctor specializing in gynecology and fetal medicine. Help interpret fetal ultrasound results."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 256,
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "LLM response unavailable."
