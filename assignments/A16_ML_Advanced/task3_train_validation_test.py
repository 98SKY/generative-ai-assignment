import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("data.csv")

df["subscriber_category"] = pd.cut(
    df["subscribers"],
    bins=[0, 100000, 1000000, 10000000, float("inf")],
    labels=["Small", "Medium", "Large", "Mega"]
)

X = df[["total_views", "total_videos"]]
y = df["subscriber_category"]

# Train 60%
# Validation 20%
# Test 20%

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.4,
    random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=42
)

best_depth = None
best_score = 0

for depth in [2, 3, 4, 5]:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_val)

    score = accuracy_score(y_val, pred)

    print(f"Depth={depth}, Validation Accuracy={score:.4f}")

    if score > best_score:
        best_score = score
        best_depth = depth

print("\nBest Depth:", best_depth)

final_model = DecisionTreeClassifier(
    max_depth=best_depth,
    random_state=42
)

final_model.fit(X_train, y_train)

final_pred = final_model.predict(X_test)

print("Test Accuracy:",
      accuracy_score(y_test, final_pred))