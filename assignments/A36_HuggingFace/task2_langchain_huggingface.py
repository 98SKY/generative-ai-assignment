from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)

llm = HuggingFacePipeline(
    pipeline=pipe
)

response = llm.invoke(
    "What is Generative AI?"
)

print("\nResponse:")
print(response)