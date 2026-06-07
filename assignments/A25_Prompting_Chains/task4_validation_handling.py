from pydantic import BaseModel, ValidationError


class Answer(BaseModel):
    answer: str
    confidence: float
    source: str


try:
    data = {
        "answer": "AI Response",
        "confidence": "wrong_type",
        "source": "PDF"
    }

    result = Answer(**data)

except ValidationError as e:
    print("Validation Error")
    print(e)