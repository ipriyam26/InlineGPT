from datetime import datetime
import openai
from .openai_auth import get_api_key


def chat(message: str) -> str:
    openai.api_key = get_api_key()
    messages = [
        {"role": "system", "content": "You are a helpful assistant.\
         Be precise and to the point."},
    ]
    word = ""
    try:
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
    except Exception:
        word = "Server is Overloaded right now, Please try again later..."
    # open loggin file
    with open("log.txt", "a") as f:
        f.write("====================================\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"User: {message}\n")
        f.write(f"Bot: {chat_completion.choices[0].message.content}\n")
    try:
        word = chat_completion.choices[0].message.content
    except Exception:
        word = "Internal Server Error, please try again later."
    return word
