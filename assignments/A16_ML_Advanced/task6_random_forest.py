import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier

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

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Decision Tree
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# Bagging
bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42
)

bagging.fit(X_train, y_train)

# Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

print(
    "Decision Tree:",
    accuracy_score(y_test, tree.predict(X_test))
)

print(
    "Bagging:",
    accuracy_score(y_test, bagging.predict(X_test))
)

print(
    "Random Forest:",
    accuracy_score(y_test, rf.predict(X_test))
)

print("\nFeature Importance")

for feature, importance in zip(
    X.columns,
    rf.feature_importances_
):
    print(
        feature,
        "->",
        round(importance, 4)
    )