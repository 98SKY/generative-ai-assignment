from langchain_core.runnables import RunnablePassthrough

chain = (
    RunnablePassthrough()
)

result = chain.invoke(
    "Hello LangChain"
)

print(result)