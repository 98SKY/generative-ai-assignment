from pydantic import BaseModel


class Answer(BaseModel):
    answer: str
    confidence: float
    source: str


response = Answer(
    answer="RAG retrieves documents before generation.",
    confidence=0.95,
    source="Knowledge Base"
)

print(response.model_dump())