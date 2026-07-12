from .ollama_backend import enhance_with_ollama
from .gemini_backend import enhance_with_gemini

def enhance_solution(prompt: str, mode: str) -> str:
    if mode == "local":
        return enhance_with_ollama(prompt)

    elif mode == "gemini":
        return enhance_with_gemini(prompt)

    else:
        raise ValueError("Invalid AI mode. Use 'local' or 'gemini'.")

def build_prompt(title, difficulty, tags, language, code):
    return f"""
You are a senior software engineer.

Problem Title: {title}
Difficulty: {difficulty}
Tags: {', '.join(tags)}
Language: {language}

Code:
{code}

Tasks:
1. Explain the approach clearly.
2. Mention time and space complexity.
3. Add a working main() function.
4. Keep it clean and concise.
"""
