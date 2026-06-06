import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
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

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Linear Kernel
linear_svm = SVC(kernel="linear")
linear_svm.fit(X_train, y_train)

linear_pred = linear_svm.predict(X_test)

linear_acc = accuracy_score(y_test, linear_pred)

# RBF Kernel
rbf_svm = SVC(kernel="rbf")
rbf_svm.fit(X_train, y_train)

rbf_pred = rbf_svm.predict(X_test)

rbf_acc = accuracy_score(y_test, rbf_pred)

print("Linear Kernel Accuracy:", linear_acc)
print("RBF Kernel Accuracy:", rbf_acc)