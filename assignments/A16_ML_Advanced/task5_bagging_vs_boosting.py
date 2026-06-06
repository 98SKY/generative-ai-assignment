import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier

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

bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42
)

bagging.fit(X_train, y_train)

bag_pred = bagging.predict(X_test)

boosting = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

boosting.fit(X_train, y_train)

boost_pred = boosting.predict(X_test)

print(
    "Bagging Accuracy:",
    accuracy_score(y_test, bag_pred)
)

print(
    "Boosting Accuracy:",
    accuracy_score(y_test, boost_pred)
)

print("\nBagging:")
print("Builds models independently and combines results.")

print("\nBoosting:")
print("Builds models sequentially and corrects previous mistakes.")