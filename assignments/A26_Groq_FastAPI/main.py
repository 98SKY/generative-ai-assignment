from fastapi import FastAPI
from pydantic import BaseModel

from chatbot import groq_chat
from groq_client import groq_chat

app = FastAPI(
    title="Groq Chatbot API",
    version="1.0"
)


# Request Model
class ChatRequest(BaseModel):
    query: str


# Response Model
class ChatResponse(BaseModel):
    answer: str


# Health Check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Groq Chatbot API"
    }


# Chat Endpoint
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = groq_chat(request.query)

    return ChatResponse(
        answer=answer
    )