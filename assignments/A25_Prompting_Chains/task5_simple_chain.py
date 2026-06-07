from langchain_core.prompts import PromptTemplate
from langchain_community.llms.fake import FakeListLLM

llm = FakeListLLM(
    responses=[
        "Generative AI creates new content."
    ]
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic}"
)

chain = prompt | llm

result = chain.invoke(
    {"topic": "Generative AI"}
)

print(result)