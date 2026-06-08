# Assignment 36: Hugging Face Integration

## Objective

Learn how to integrate Hugging Face models with LangChain and use them as alternatives to OpenAI and Groq models.

---

## Task 1: Getting Started with Hugging Face Models

Implemented:

* Loaded Hugging Face model
* Used google/flan-t5-base
* Generated response for a simple prompt

Observation:

The model successfully generated responses without requiring OpenAI APIs.

---

## Task 2: Hugging Face with LangChain

Implemented:

* Integrated Hugging Face Pipeline with LangChain
* Replaced OpenAI model with Hugging Face model
* Tested multiple prompts

Observation:

LangChain chains work seamlessly with Hugging Face models.

---

## Task 3: ChatPromptTemplate with Hugging Face

Implemented:

* ChatPromptTemplate
* System message
* Human message
* Hugging Face backed LLM

Observation:

ChatPromptTemplate provides a cleaner structure than standard PromptTemplate and better supports conversational workflows.

---

## Comparison

### Normal Prompt Template

Advantages:

* Simpler
* Good for one-shot tasks

Disadvantages:

* Limited conversational structure

### Chat Prompt Template

Advantages:

* Supports system messages
* Better conversation management
* Easier integration with chat-based applications

Disadvantages:

* Slightly more verbose

---

## Conclusion

Hugging Face models can effectively replace proprietary APIs for many GenAI tasks. LangChain provides seamless integration and allows developers to build prompt-driven applications using open-source models.
