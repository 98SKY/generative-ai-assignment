questions = [

    "Who earns more?",

    "Show sales.",

    "Which department is best?"
]

for q in questions:

    print("\nQuestion:")
    print(q)

    result = agent.invoke(
        {"input": q}
    )

    print(result["output"])