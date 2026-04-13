import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# učitaj podatke
df = pd.read_csv('occupancy_processed.csv')

feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()

# a) podjela skupa (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# b) skaliranje
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# c) KNN model
K = 5
knn = KNeighborsClassifier(n_neighbors=K)
knn.fit(X_train_scaled, y_train)

# predikcija
y_pred = knn.predict(X_test_scaled)

# d) evaluacija
print("K=" + str(K))
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

print("\nTočnost:")
print(accuracy_score(y_test, y_pred))

print("\nPreciznost po klasama:")
print(precision_score(y_test, y_pred, average=None))

print("\nOdziv po klasama:")
print(recall_score(y_test, y_pred, average=None))