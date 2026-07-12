import os
from leetsync.config import GEMINI_API_KEY
from google import genai

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment.")

client = genai.Client(api_key=GEMINI_API_KEY)


def enhance_with_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return ""
