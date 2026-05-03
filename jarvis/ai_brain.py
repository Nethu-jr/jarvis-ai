import requests

def ask_ollama(text):
    try:
        prompt = f"""
You are Jarvis, an intelligent screen analyzer.

You MUST follow these rules strictly:

1. DO NOT greet.
2. DO NOT say "Hello" or "What can I help".
3. ONLY explain what is visible on the screen.
4. Ignore random symbols or garbage text.
5. If it's code → explain code.
6. If it's a website → explain what page it is.
7. Be direct and clear.
8. If text is unclear → say "Screen content is not clear".

SCREEN TEXT:
{text}

Now explain the screen content:
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json().get("response", "No response")

    except Exception as e:
        print("Error:", e)
        return "AI error"