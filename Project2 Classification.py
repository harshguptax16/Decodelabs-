"""
=======================================================================
DecodeLabs - AI Internship : Project 2
Data Classification using AI
=======================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import(
    confusion_matrix,
    accuracy_score,
    f1_score,
    classification_report
)

#------------------------------------------------------------
#STEP 1 (INPUT): Load and Understand the Dataset
#------------------------------------------------------------
print("=" * 60)
print("STEP 1: Loading & Understanding Dataset (Iris Benchmark)")
print("=" * 60)

iris = load_iris()
x = iris.data
y = iris.target

df = pd.DataFrame(x, columns=iris.feature_names)
df["species"] = [iris.target_name[i] for i in y]

print(f"\nTotal Samples : {df.shape[0]}")
print(f"Total Features: {x.shape[1]}")
print(f"Classes       : {list(iris.target_names)}")
print("\nFirst 5 rows of dataset:\n", df.head())
print("\nClass Distribution (balanced check):\n", df["species"].value_counts())

#-------------------------------------------------------------
#STEP 2 (INPUT - Gatekeeper Rule): Feature Scaling
#-------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 2: Feature Scaling (StandardScaler: mean=0, variance=1)")
print("=" * 60)

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print("Scaling done. Example (First row) BEFORE vs AFTER scaling:")
print("Before:", x[0])
print("After:", np.round(x_scaled[0], 2))

#--------------------------------------------------------------
#STEP 3 (PROCESS - Structural Integrity): Train-Test Split
#--------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 3: Train-Test Split (80% train, 20% test, shuffled)")
print("=" * 60)

x_train, x_test, y_train, y_test = train_test_split(
    x_scaled, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training samples: {x_train.shape[0]}")
print(f"Training samples: {x_test.shape[0]}")

#--------------------------------------------------------------
#STEP 4 (Tunig the Engine): Choosing Best K (Elbow Method)
#--------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 4: Finding Optimal K (Elbow Method)")
print("=" * 60)

error_rates = []
k_range = range(1, 21)

for k in k_range:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(x_train, y_train)
    pred_temp = knn_temp.predict(x_test)
    error_rates.append(np.mean(pred_temp != y_test))
    
# NOTE: We avoid blindly picking the raw minimum-error K, because K=1
# often "wins" onerror rate but is actually Overfitting (memorizing
# noise, as warned in the training slides). A true "elbow" pick is the
# smallest K >= 3 whose error is within a small tolerance of the best
# error seen -- this favors a more generalizable, stable model.
min_error = min(error_rates)
tolerance = 0.02
candidates = [k for k, err in zip(k_range, error_rates)
              if err <= min_error + tolerance and k >= 3]
best_k = candidates[0] if candidates else k_range[np.argmin(error_rates)]
print(f"Best K found at the 'elbow' (robust, avoids k=1 overfitting): K ={best_k}")

plt.figure(figsize=(8, 5))
plt.plot(k_range, error_rates, marker="o", linestyle="--", color="darkblue")
plt.axvline(best_k, color="orange", linestyle=":", label=f"Optimal k = {best_k}")
plt.title("Tuning the Engine: Error Rate vs K Value")
plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("elbow_curve.png", dpi=150)
print("Saved elbow curve plot -i elbow_curve.png")

#---------------------------------------------------------------
#STEP 5 (PROCESS - Sickit-learn Workflow): Train Final Model
#---------------------------------------------------------------
print("\n" + "=" * 60)
print(f"STEP 5: Training Final KNN Model (K = {best_k})")
print("=" * 60)

model = KNeighborsClassifier(n_neighbours=best_k)
model.fit(x_train, y_train)
predictions = model.predict(x_test)

print("Model trained successfully!")

#---------------------------------------------------------------
#STEP 6 (OUTPUT): Confusion Matrix + Accuracy + F1 Score
#---------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 6: Output Validation (Don't trust accuracy alone!)")
print("=" + 60)

acc = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="weighted")
cm = confusion_matrix(y_test, predictions)

print(f"\nAccuracy : {acc:.4f} ({acc*100:.2f}%)")
print(f"F1 Score : {f1:.4f} (weighted average)")

print("\nfull Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))

#Confusion Matrix heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)
plt.title("Confusion Matrix: The Diagnostic Tool")
plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
print("\nSaved Confusion matrix plot -> confusion_matrix.png")

print("\n" + "=" * 60)
print("PROJECT 2 COMPLETE - Milestone Unlocked! ")
print("=" * 60)