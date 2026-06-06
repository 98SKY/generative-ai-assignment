import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
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

# Underfitting
tree_small = DecisionTreeClassifier(max_depth=2)
tree_small.fit(X_train, y_train)

# Overfitting
tree_large = DecisionTreeClassifier(max_depth=None)
tree_large.fit(X_train, y_train)

print("Underfitting Model")
print("Train:", accuracy_score(y_train, tree_small.predict(X_train)))
print("Test :", accuracy_score(y_test, tree_small.predict(X_test)))

print("\nOverfitting Model")
print("Train:", accuracy_score(y_train, tree_large.predict(X_train)))
print("Test :", accuracy_score(y_test, tree_large.predict(X_test)))

plt.figure(figsize=(10, 6))
plot_tree(
    tree_small,
    feature_names=X.columns,
    filled=True,
    max_depth=2
)

plt.show()