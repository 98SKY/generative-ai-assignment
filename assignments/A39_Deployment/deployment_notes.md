# Deployment Notes – Assignment 39

## Project Information

Project Name: ChatGroq RAG Chatbot

Technology Stack:

* Python
* Streamlit
* LangChain
* Groq API
* FAISS
* Hugging Face Embeddings

---

# Deployment 1: Streamlit Cloud

## Deployment Steps

1. Created GitHub repository.
2. Uploaded project source code.
3. Added requirements.txt.
4. Logged into Streamlit Community Cloud.
5. Connected GitHub repository.
6. Selected app.py as entry point.
7. Added environment variables using Streamlit Secrets.
8. Deployed application.

## Environment Variables

GROQ_API_KEY=<your_api_key>

## Result

Application deployed successfully and accessible through a public URL.

## Validation Performed

* Application loaded successfully.
* Document upload worked correctly.
* Questions were answered from uploaded documents.
* Error handling verified.

---

# Deployment 2: Hugging Face Spaces

## Deployment Steps

1. Created a new Streamlit Space.
2. Uploaded source code.
3. Added requirements.txt.
4. Configured environment variables in Space settings.
5. Waited for build completion.
6. Tested deployed application.

## Environment Variables

GROQ_API_KEY=<your_api_key>

## Result

Application deployed successfully and accessible through a public URL.

## Validation Performed

* Application launched successfully.
* User document upload worked.
* RAG pipeline returned grounded answers.
* Chat interface functioned correctly.

---

# Challenges Faced

## Dependency Installation Issues

Some packages required version updates.

Resolution:

* Updated requirements.txt
* Rebuilt deployment

## Environment Variable Configuration

Groq API key was initially missing.

Resolution:

* Added secret variables in deployment settings.

## Build Time Delays

Hugging Face Space required additional build time.

Resolution:

* Waited for build completion and checked logs.

---

# Performance Observations

## Streamlit Cloud

Advantages:

* Faster deployment
* Easy GitHub integration
* Suitable for prototypes

Limitations:

* Limited compute resources

## Hugging Face Spaces

Advantages:

* AI-focused hosting
* Better support for ML applications
* Optional GPU availability

Limitations:

* Longer build times

---

# Conclusion

The ChatGroq RAG application was successfully deployed on both Streamlit Cloud and Hugging Face Spaces. Both platforms provided reliable hosting for the GenAI application. Streamlit Cloud offered simpler deployment, while Hugging Face Spaces provided a more AI-focused environment suitable for future production-scale GenAI applications.


## Deployment URLs

Streamlit Cloud URL:
https://your-app.streamlit.app

Hugging Face Space URL:
https://huggingface.co/spaces/username/project-name