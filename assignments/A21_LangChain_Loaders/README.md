# Assignment 21: LangChain Document Loaders & Text Splitters

## Objective

Learn how to load data from multiple sources using LangChain and split large documents into manageable chunks for GenAI applications.

## Topics Covered

- TextLoader
- CSVLoader
- PyPDFLoader
- DirectoryLoader
- WebBaseLoader
- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- Document Chunking

## How To Run

Install dependencies:

```bash
pip install langchain
pip install langchain-community
pip install pypdf
pip install beautifulsoup4
pip install unstructured
```

Run tasks:

```bash
python task1_text_loader.py
python task2_csv_loader.py
python task3_pdf_loader.py
python task4_directory_loader.py
python task5_web_loader.py
python task7_character_splitter.py
python task8_recursive_splitter.py
python task9_document_splitter.py
python task11_unified_pipeline.py
```

## Learning Outcome

- Load text, CSV, PDF, folders, and websites.
- Understand document chunking.
- Learn different text splitting strategies.
- Prepare data for future RAG applications.