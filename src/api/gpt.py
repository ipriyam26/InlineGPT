import openai
from .openai_auth import get_api_key


def chat(message: str) -> str:
    openai.api_key = get_api_key()
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Be precise and to the point."},
    ]

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    word = ""
    # open loggin file
    with open("log.txt", "a") as f:
        f.write(f"User: {message}\n")
        f.write(f"Bot: {chat_completion.choices[0].text}\n")
    try:
        word = chat_completion.choices[0].text
    except Exception:
        word = "ok"
    return word
