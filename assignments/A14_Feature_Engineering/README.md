# Assignment 14: Feature Engineering, Encoding, Scaling & Pipelines

## Objective

This assignment demonstrates:

* Feature Engineering
* Feature Encoding
* Feature Scaling
* ColumnTransformer
* Scikit-learn Pipelines
* End-to-End Machine Learning Workflow

Dataset used: YouTube Channel Analytics Dataset

---

## Folder Structure

A14_Feature_Engineering/

├── feature_engineering_assignment.py

├── data.csv

└── README.md

---

## Tasks Covered

### Task 1: Feature Engineering

Created new features:

* avg_views_per_video
* subs_per_video
* subscriber_category

### Task 2: Date & Text Features

Extracted:

* created_year
* created_month
* created_day

Created text-based features:

* channel_name_length
* description_length

### Task 3: One-Hot Encoding

Applied:

* pd.get_dummies()

### Task 4: ColumnTransformer

Separated:

* Numerical features
* Categorical features

Applied:

* OneHotEncoder
* StandardScaler

### Task 5: Standardization

Applied:

* StandardScaler

### Task 6: Normalization

Applied:

* MinMaxScaler

### Task 7: Preprocessing Pipeline

Built reusable preprocessing pipeline using:

* Pipeline
* ColumnTransformer

### Task 8: Full Scikit-learn Pipeline

Workflow:

Raw Data → Encoding → Scaling → Linear Regression Model

Steps:

* Train-Test Split
* Fit Pipeline
* Predict Test Data

### Task 9: Pipeline Benefits

Explained:

* Importance of pipelines
* Problems solved by pipelines
* Manual vs Pipeline preprocessing

---

## Requirements

Install dependencies:

```bash
pip install pandas numpy scikit-learn
```

---

## How to Run

```bash
cd A14_Feature_Engineering

python feature_engineering_assignment.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## Author

Sunil Kumar
