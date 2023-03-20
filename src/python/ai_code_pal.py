import requests
import os

def get_chatgpt_suggestion(code_snippet):
    api_key = os.environ.get('OPENAI_API_KEY')
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": f"Improve the following Python code: {code_snippet}",
        "max_tokens": 50,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }
    response = requests.post(url, headers=headers, json=data)
    suggestion = response.json()['choices'][0]['text']
    return suggestion.strip()

