from typing import Tuple
import openai


OPENAI_MODEL = "gpt-3.5-turbo"


def get_chatgpt_suggestion(code_snippet: str) -> Tuple[str, int]:
    """
    Returns PR style feedback for the given code snippet, and the number of tokens used.
    """
    system_prompt = f"""You are AI Code Pal. Suggest improvements to the provided Python code as in a code review."""

    user_prompt = code_snippet
    llm_response = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    )

    return llm_response["choices"][0]["message"]["content"].strip(), llm_response["usage"]["total_tokens"]

