import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
    MinMaxScaler
)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score



# LOAD DATA


print("\n========== LOADING DATA ==========\n")

df = pd.read_csv("data.csv")
print(df.columns)

print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())



# TASK 1: FEATURE ENGINEERING

print("\n========== TASK 1: FEATURE ENGINEERING ==========\n")

# Average views per video
df["avg_views_per_video"] = np.where(
    df["total_videos"] > 0,
    df["total_views"] / df["total_videos"],
    0
)

# Subscribers per video
df["subs_per_video"] = np.where(
    df["total_videos"] > 0,
    df["subscribers"] / df["total_videos"],
    0
)

# Subscriber category
df["subscriber_category"] = pd.cut(
    df["subscribers"],
    bins=[0, 100000, 1000000, 10000000, np.inf],
    labels=["Small", "Medium", "Large", "Mega"]
)

print(
    df[
        [
            "subscribers",
            "avg_views_per_video",
            "subs_per_video",
            "subscriber_category"
        ]
    ].head()
)



# TASK 2: DATE & TEXT FEATURES


print("\n========== TASK 2: DATE & TEXT FEATURES ==========\n")

df["created_date"] = pd.to_datetime(
    df["created_date"],
    format="ISO8601",
    errors="coerce"
)

df["scraped_at"] = pd.to_datetime(
    df["scraped_at"],
    format="ISO8601",
    errors="coerce"
)

df["created_year"] = df["created_date"].dt.year
df["created_month"] = df["created_date"].dt.month
df["created_day"] = df["created_date"].dt.day

df["channel_name_length"] = (
    df["channel_name"]
    .astype(str)
    .apply(len)
)

df["description_length"] = (
    df["description"]
    .astype(str)
    .apply(len)
)

print(
    df[
        [
            "created_year",
            "created_month",
            "created_day",
            "channel_name_length",
            "description_length"
        ]
    ].head()
)



# TASK 3: ONE HOT ENCODING


print("\n========== TASK 3: ONE HOT ENCODING ==========\n")

encoded_df = pd.get_dummies(
    df,
    columns=[
        "country",
        "subscriber_category"
    ],
    drop_first=True
)

print(encoded_df.head())



# TASK 4: COLUMN TRANSFORMER


print("\n========== TASK 4: COLUMN TRANSFORMER ==========\n")

target = "subscribers"

numerical_cols = [
    "total_videos",
    "total_views",
    "avg_views_per_video",
    "subs_per_video",
    "channel_name_length",
    "description_length"
]

categorical_cols = [
    "country"
]

features = numerical_cols + categorical_cols

X = df[features]
y = df[target]

print("Numerical Columns:")
print(numerical_cols)

print("\nCategorical Columns:")
print(categorical_cols)



# TASK 5: STANDARDIZATION


print("\n========== TASK 5: STANDARD SCALER ==========\n")

standard_scaler = StandardScaler()

scaled_data = standard_scaler.fit_transform(
    X[numerical_cols]
)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=numerical_cols
)

print(scaled_df.head())

print("\nMeans:")
print(np.round(scaled_df.mean(), 4))

print("\nStandard Deviations:")
print(np.round(scaled_df.std(), 4))



# TASK 6: MINMAX SCALER


print("\n========== TASK 6: MINMAX SCALER ==========\n")

minmax_scaler = MinMaxScaler()

normalized_data = minmax_scaler.fit_transform(
    X[numerical_cols]
)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=numerical_cols
)

print(normalized_df.head())

print("\nMinimum Values:")
print(normalized_df.min())

print("\nMaximum Values:")
print(normalized_df.max())



# TASK 7: PREPROCESSING PIPELINE


print("\n========== TASK 7: PREPROCESSING PIPELINE ==========\n")

numeric_pipeline = Pipeline([
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    (
        "encoder",
        OneHotEncoder(handle_unknown="ignore")
    )
])

preprocessor = ColumnTransformer([
    (
        "num",
        numeric_pipeline,
        numerical_cols
    ),
    (
        "cat",
        categorical_pipeline,
        categorical_cols
    )
])

transformed_data = preprocessor.fit_transform(X)

print("Transformed Shape:")
print(transformed_data.shape)



# TASK 8: FULL SCIKIT-LEARN PIPELINE


print("\n========== TASK 8: FULL ML PIPELINE ==========\n")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

model_pipeline.fit(
    X_train,
    y_train
)

predictions = model_pipeline.predict(
    X_test
)

print("First 10 Predictions:")
print(predictions[:10])

# Evaluation
mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nModel Evaluation")
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 4))



# TASK 9: PIPELINE BENEFITS


print("\n========== TASK 9: PIPELINE BENEFITS ==========\n")

print("""
1. Why are Pipelines Important?

Pipelines automate preprocessing and model training
into one workflow. This makes ML projects cleaner,
reproducible, and easier to maintain.

------------------------------------------------

2. What Problems do Pipelines Solve?

• Reduce repetitive code
• Prevent data leakage
• Ensure consistent preprocessing
• Simplify deployment
• Improve maintainability

------------------------------------------------

3. Manual vs Pipeline-Based Preprocessing

Manual Preprocessing:
• Multiple preprocessing steps written separately
• Higher chance of mistakes
• Difficult to reuse

Pipeline-Based Preprocessing:
• Everything handled automatically
• Cleaner code
• Reusable workflow
• Better for production systems
""")

print("\n========== ASSIGNMENT COMPLETED ==========\n")