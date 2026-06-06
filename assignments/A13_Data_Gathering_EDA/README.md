# Assignment 13: Data Gathering, Preprocessing & Exploratory Data Analysis (EDA)

## Overview

This assignment demonstrates the complete workflow of:

* Data Gathering from multiple sources (CSV, JSON, SQLite Database, API)
* Data Preprocessing & Cleaning
* Feature Preparation
* Exploratory Data Analysis (EDA)

The implementation is done using a single Python file as required.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite3
* Requests

---

## Project Structure

```
A13_Data_Gathering/
│
├── assignment13_eda.py
├── data.csv
├── data.json
├── sample.db               (auto-created)
├── tmdb_movies.csv         (generated from API)
└── README.md
```

---

## Tasks Covered

### Part 1: Data Gathering

#### Task 1: Load Data from CSV

* Load CSV dataset using Pandas
* Display:

  * Shape
  * Column names
  * First 5 rows

#### Task 2: Load Data from JSON

* Read JSON file
* Convert JSON data into DataFrame
* Display DataFrame

#### Task 3: Load Data from SQLite Database

* Create SQLite database
* Create employees table
* Insert sample records
* Read data using SQL query
* Convert results into DataFrame

#### Task 4: API Mini Project (TMDB API)

* Fetch movie data using Requests library
* Extract:

  * Movie Title
  * Release Date
  * Rating
  * Popularity
* Store results in CSV

---

## Part 2: Data Preprocessing & Cleaning

### Task 5: Understanding the Data

* Dataset shape
* Data types
* Missing values
* Numerical and categorical columns

### Task 6: Data Cleaning

* Handle missing values
* Remove duplicate records
* Rename columns
* Fix data types

### Task 7: Feature Preparation

* Encode categorical variables
* Prepare features for machine learning

---

## Part 3: Exploratory Data Analysis (EDA)

### Task 8: Univariate Analysis

* Histograms
* KDE plots
* Boxplots
* Distribution analysis

### Task 9: Bivariate Analysis

* Scatter plots
* Correlation heatmap
* Bar plots
* Box plots

### Task 10: Insights & Observations

* Data patterns
* Outliers
* Relationships between variables
* Data quality observations

---

## Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn requests
```

---

## How to Run

Navigate to the project directory:

```bash
cd A13_Data_Gathering
```

Run the Python file:

```bash
python assignment13_eda.py
```

---

## Expected Output

The program will:

1. Load data from CSV, JSON, SQLite, and API sources.
2. Display dataset information.
3. Perform data cleaning operations.
4. Generate EDA visualizations.
5. Print key insights and observations.

---

## Learning Outcomes

By completing this assignment, I learned:

* Working with multiple data sources
* Data cleaning techniques
* Feature engineering basics
* Exploratory Data Analysis (EDA)
* Data visualization using Matplotlib and Seaborn
* Preparing datasets for Machine Learning

---

## Author

Sunil Kumar
Full Stack Developer | Learning Data Science & Machine Learning
