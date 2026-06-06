# Assignment 17: Text Cleaning, Preprocessing & NLP Pipeline

## Dataset

Custom Product Reviews Dataset

Source:
Self-created dataset (reviews.csv)

## Topics Covered

- Basic Text Cleaning
- Advanced Text Cleaning
- Stopword Removal
- Tokenization
- Stemming
- Lemmatization
- NLP Pipeline

## Install Dependencies

```bash
pip install pandas nltk
```

## Download NLTK Resources

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## Run Tasks

```bash
python task1_raw_text.py
python task2_basic_cleaning.py
python task3_remove_noise.py
python task4_stopwords.py
python task5_slang_normalization.py
python task6_tokenization.py
python task7_stemming.py
python task8_lemmatization.py
python task9_nlp_pipeline.py
```