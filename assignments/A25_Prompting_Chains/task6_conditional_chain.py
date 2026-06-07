def answer_question(question):

    factual_keywords = [
        "what",
        "when",
        "where",
        "who"
    ]

    if any(
        word in question.lower()
        for word in factual_keywords
    ):
        return "Using Retriever"

    return "Using Direct LLM"


print(
    answer_question(
        "What is RAG?"
    )
)

print(
    answer_question(
        "Write a poem on AI"
    )
)