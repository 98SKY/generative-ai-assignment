# Observations & Insights

## 1. Difference between PDF Q&A and Conversational PDF Q&A

PDF Q&A answers each question independently.

Conversational PDF Q&A uses previous interactions to understand follow-up questions.

---

## 2. Role of Message History

Message history provides context for follow-up questions.

Without history, the chatbot may not understand references such as:

"Explain that more"

"What about the previous topic?"

---

## 3. Trade-offs Between Long Memory and Performance

Long memory improves contextual understanding.

However it increases:

- token usage
- latency
- cost

---

## 4. How Trimming Affects Answer Quality

Trimming reduces memory usage and improves speed.

Excessive trimming may remove important context and reduce answer quality.