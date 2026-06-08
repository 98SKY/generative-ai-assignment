import os

from groq import Groq

from dotenv import load_dotenv

from prompts import (
    GENERATE_CODE_PROMPT,
    EXPLAIN_CODE_PROMPT,
    DEBUG_CODE_PROMPT,
    OPTIMIZE_CODE_PROMPT
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"


def ask_llm(prompt):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def generate_code(query):
    return ask_llm(
        GENERATE_CODE_PROMPT.format(query=query)
    )


def explain_code(code):
    return ask_llm(
        EXPLAIN_CODE_PROMPT.format(query=code)
    )


def debug_code(code):
    return ask_llm(
        DEBUG_CODE_PROMPT.format(query=code)
    )


def optimize_code(code):
    return ask_llm(
        OPTIMIZE_CODE_PROMPT.format(query=code)
    )