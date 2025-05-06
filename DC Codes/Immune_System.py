import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from collections import namedtuple

# Step 1: Generate synthetic data for 3 types of structure conditions (Healthy, Minor Damage, Severe Damage)
def generate_structural_data(n_samples=300):
    np.random.seed(42)
    # Class 0: Healthy
    class_0 = np.random.normal(loc=[0.2, 0.1, 0.3], scale=0.05, size=(n_samples, 3))
    # Class 1: Minor Damage
    class_1 = np.random.normal(loc=[0.5, 0.6, 0.4], scale=0.07, size=(n_samples, 3))
    # Class 2: Severe Damage
    class_2 = np.random.normal(loc=[0.9, 0.8, 0.7], scale=0.05, size=(n_samples, 3))
    # Combine all data
    X = np.vstack((class_0, class_1, class_2))
    y = np.array([0]*n_samples + [1]*n_samples + [2]*n_samples)
    return X, y

# Step 2: Preprocess the data (normalize and split)
X, y = generate_structural_data()
scaler = MinMaxScaler()
X = scaler.fit_transform(X)  # Normalize between 0 and 1

# 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Define Antibody structure using namedtuple for clarity
Antibody = namedtuple("Antibody", ["features", "label", "affinity"])

# Step 4: Define the Artificial Immune System (AIS) Classifier
class AISClassifier:
    def __init__(self, n_clones=10, n_generations=20):
        self.memory_cells = []
        self.n_clones = n_clones
        self.n_generations = n_generations

    # Affinity: Inverse of distance (higher means better match)
    def affinity(self, a, b):
        return 1.0 / (1.0 + np.linalg.norm(a - b))

    # Training: Create antibodies, mutate clones, keep top N best detectors
    def train(self, X, y):
        for _ in range(self.n_generations):
            population = [Antibody(x, label, 1.0) for x, label in zip(X, y)]
            clones = []

            for ab in population:
                for _ in range(self.n_clones):
                    # Create mutated version of the antibody
                    mutation = ab.features + np.random.normal(0, 0.1, size=len(ab.features))
                    mutated = np.clip(mutation, 0, 1)  # Keep in range [0, 1]
                    clones.append(Antibody(mutated, ab.label, self.affinity(mutated, ab.features)))

            # Combine population and clones, sort by affinity
            all_ab = population + clones
            all_ab.sort(key=lambda x: x.affinity, reverse=True)
            self.memory_cells = all_ab[:len(set(y)) * 10]  # Keep top N per class

    # Predict: Find best matching antibody
    def predict(self, X):
        predictions = []
        for x in X:
            best = max(self.memory_cells, key=lambda ab: self.affinity(x, ab.features))
            predictions.append(best.label)
        return np.array(predictions)

# Step 5: Train and Evaluate
model = AISClassifier()
model.train(X_train, y_train)
predictions = model.predict(X_test)

# Show classification results
print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Step 6: Plot Results
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=predictions, cmap="viridis", marker='o', label="Predicted")
plt.title("AIS Classification Results (Test Data)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.colorbar(label="Predicted Class")
plt.grid(True)
plt.show()