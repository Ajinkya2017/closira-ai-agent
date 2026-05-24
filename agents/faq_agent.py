from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from utils.prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

with open("sop_data.json", "r") as file:
    sop_data = json.load(file)


def faq_response(user_input):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT + f"\n\nSOP DATA:\n{sop_data}"
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content