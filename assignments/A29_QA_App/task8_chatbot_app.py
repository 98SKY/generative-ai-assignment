from task7_model_switch import get_answer

model = input(
    "Choose model (groq/ollama): "
)

while True:

    question = input(
        "\nYou: "
    )

    if question.lower() == "exit":
        break

    answer = get_answer(
        question,
        model
    )

    print("\nBot:", answer)