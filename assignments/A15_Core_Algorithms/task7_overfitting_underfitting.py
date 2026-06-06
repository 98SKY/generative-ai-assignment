import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data.csv")

df["subscriber_category"] = pd.cut(
    df["subscribers"],
    bins=[0, 100000, 1000000, 10000000, float("inf")],
    labels=["Small", "Medium", "Large", "Mega"]
)

X = df[["total_views", "total_videos"]]
y = df["subscriber_category"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Underfitting
simple_model = DecisionTreeClassifier(max_depth=1)

simple_model.fit(X_train, y_train)

train_acc = accuracy_score(
    y_train,
    simple_model.predict(X_train)
)

test_acc = accuracy_score(
    y_test,
    simple_model.predict(X_test)
)

print("UNDERFITTING")
print("Train Accuracy:", train_acc)
print("Test Accuracy :", test_acc)

# Overfitting
complex_model = DecisionTreeClassifier(max_depth=None)

complex_model.fit(X_train, y_train)

train_acc = accuracy_score(
    y_train,
    complex_model.predict(X_train)
)

test_acc = accuracy_score(
    y_test,
    complex_model.predict(X_test)
)

print("\nOVERFITTING")
print("Train Accuracy:", train_acc)
print("Test Accuracy :", test_acc)