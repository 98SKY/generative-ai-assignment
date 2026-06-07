from langchain_core.runnables import RunnableParallel

parallel = RunnableParallel(
    answer=lambda x:
        f"Answer: {x}",

    summary=lambda x:
        f"Summary: {x[:10]}",

    followup=lambda x:
        "What else would you like to know?"
)

result = parallel.invoke(
    "Generative AI is transforming software."
)

print(result)