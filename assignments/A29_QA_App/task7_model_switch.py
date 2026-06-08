import os

from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def get_answer(
    question,
    model_type="groq"
):

    if model_type == "groq":

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    elif model_type == "ollama":

        return "Ollama answer"

print(
    get_answer(
        "What is AI?"
    )
)