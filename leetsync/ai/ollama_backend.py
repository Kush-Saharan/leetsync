import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"

def enhance_with_ollama(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        return ""

    return response.json().get("response", "")
