import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree

dataset = {
    "Toothed": [1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    "Hair": [1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    "Breathes": [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    "Legs": [1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
    "species": [
        "Mammal",
        "Mammal",
        "Reptile",
        "Mammal",
        "Mammal",
        "Mammal",
        "Reptile",
        "Reptile",
        "Mammal",
        "Reptile",
    ],
}

df = pd.DataFrame(dataset)
print("Training Dataset:")
print(df)


feature_cols = ["Toothed", "Hair", "Breathes", "Legs"]
X = df[feature_cols]
y = df["species"]


clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100)
clf_entropy = clf_entropy.fit(X, y)


newExample = pd.DataFrame(
    [[1, 1, 0, 1]], columns=["Toothed", "Hair", "Breathes", "Legs"]
)
prediction = clf_entropy.predict(newExample)
print("\nPredicted species for new example:", prediction[0])


plt.figure(figsize=(12, 8))
plot_tree(
    clf_entropy,
    filled=True,
    feature_names=feature_cols,
    class_names=["Mammal", "Reptile"],
    rounded=True,
)
plt.savefig("animal_decision_tree.png")
plt.show()