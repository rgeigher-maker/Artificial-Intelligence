# Relevant Libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


def importdata(filepath="cleaned_merged_heart_dataset.csv"):
    data = pd.read_csv(filepath)

    print("Dataset Length:", len(data))
    print("Dataset Shape:", data.shape)
    print("\nDataset Info:")
    print(data.info())
    print("\nDataset Preview (First 10 Rows):")
    print(data.head(10))

    data = data.dropna()
    return data


def splitdataset(data):
    target_col = "target" if "target" in data.columns else data.columns[-1]
    X = data.drop(columns=[target_col])
    y = data[target_col]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=100, stratify=y
    )
    return X_train, X_test, y_train, y_test, list(X.columns), [str(c) for c in sorted(y.unique())]


def train_using_gini(X_train, y_train):
    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100)
    clf_gini.fit(X_train, y_train)
    return clf_gini


def train_using_entropy(X_train, y_train):
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100)
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


def cal_accuracy(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print(f"Accuracy : {acc * 100:.2f}% ({acc:.4f})")
    print("Report :")
    print(classification_report(y_test, y_pred))


def plot_decision_tree(clf_object, feature_names, class_names):
    plt.figure(figsize=(15, 10))
    plot_tree(
        clf_object,
        filled=True,
        feature_names=feature_names,
        class_names=class_names,
        rounded=True,
    )
    plt.show()


if __name__ == "__main__":
    data = importdata("cleaned_merged_heart_dataset.csv")
    X_train, X_test, y_train, y_test, feature_names, class_names = splitdataset(data)

    clf_gini = train_using_gini(X_train, y_train)
    clf_entropy = train_using_entropy(X_train, y_train)

    print("Results (Gini Index):")
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("Results (Entropy Index):")
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)

    plot_decision_tree(clf_gini, feature_names, class_names)
    plot_decision_tree(clf_entropy, feature_names, class_names)





