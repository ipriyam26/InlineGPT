import openai
from .openai_auth import get_api_key

def chat(message:str):
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
    return chat_completion.choices[0].message.content