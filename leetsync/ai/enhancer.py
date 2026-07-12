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
You are a senior software engineer reviewing a LeetCode solution.

Input:
- Problem Title: {title}
- Difficulty: {difficulty}
- Language: {language}

Code:
{code}

Your task is to explain ONLY the code that is provided.

Requirements:
- Do NOT explain or summarize the problem statement.
- Do NOT describe an algorithm that is not present in the code.
- Do NOT suggest optimizations or alternative approaches.
- Base every statement solely on the implementation.
- If something cannot be determined from the code alone, do not assume it.

Output a concise comment block in the following format:

/*
Approach:
- Explain how this implementation works in 3-6 bullet points.
- Mention the purpose of the main data structures, variables, and loops.
- Explain any important conditions or helper functions.

Time Complexity:
- State the actual worst-case time complexity of THIS implementation and briefly justify it.

Space Complexity:
- State the auxiliary space complexity of THIS implementation and briefly justify it.
*/

Keep the explanation under 150 words.
Do not output anything except the comment block.
"""
