print("Conversational RAG Chatbot")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    print("\nBot:")
    print("Answer generated from RAG pipeline")