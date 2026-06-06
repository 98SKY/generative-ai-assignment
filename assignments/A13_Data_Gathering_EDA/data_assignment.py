import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import requests
import json

# task 1

df = pd.read_csv("data/data.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print("First 5 rows:\n", df.head())


# task 2

with open("data/product.json", "r") as file:
    data = json.load(file)

df_json = pd.DataFrame(data)
print(df_json.head())

# task 3

print("\n===== TASK 3: SQLITE =====")

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, "John", "IT", 50000),
    (2, "Alice", "HR", 40000),
    (3, "Bob", "Finance", 60000),
    (4, "Emma", "IT", 55000),
    (5, "David", "HR", 45000)
])

conn.commit()

df_sql = pd.read_sql_query("SELECT * FROM employees", conn)
print(df_sql)

conn.close()

 # task 4
print("\n===== TASK 4: API DATA =====")

API_KEY = ""

url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    movies = response.json()["results"]

    movie_data = []
    for m in movies:
        movie_data.append({
            "title": m["title"],
            "release_date": m["release_date"],
            "rating": m["vote_average"],
            "popularity": m["popularity"]
        })

    df_movies = pd.DataFrame(movie_data)
    print(df_movies.head())

    df_movies.to_csv("tmdb_movies.csv", index=False)
else:
    print("API Error")

# task 5
print("\n===== TASK 5: UNDERSTANDING DATA =====")

print(df.info())
print("\nMissing values:\n", df.isnull().sum())

# task 6
print("\n===== TASK 6: CLEANING =====")

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

print("Cleaned Data:\n", df.head())

 # task 7

print("\n===== TASK 7: FEATURE ENGINEERING =====")

# Example encoding
df_encoded = pd.get_dummies(df, drop_first=True)

print(df_encoded.head())

# task 8
print("\n===== TASK 8: UNIVARIATE =====")

df.hist(figsize=(10, 6))
plt.show()

sns.boxplot(data=df)
plt.show()

# # task 9

print("\n===== TASK 9: BIVARIATE =====")

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# task 10

print("\n===== TASK 10: INSIGHTS =====")

print("""
1. Some columns had missing values which were filled using mean.
2. Duplicate rows were removed.
3. Certain features show strong correlation.
4. Data distribution shows presence of outliers.
5. Encoded categorical variables for ML readiness.
""")