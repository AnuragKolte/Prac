import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from geneticalgorithm import geneticalgorithm as ga  # Make sure it's installed: pip install geneticalgorithm

# Step 1: Generate sample data
# Features: [Inlet Temp, Feed Rate, Solids Content]
np.random.seed(42)
X = np.random.uniform(low=[160, 5, 10], high=[200, 20, 30], size=(100, 3))  # 100 samples
y = (
    0.1 * (200 - X[:, 0]) +      # Inlet Temp influence
    0.05 * (20 - X[:, 1]) +      # Feed Rate influence
    0.03 * (30 - X[:, 2]) +      # Solids Content influence
    np.random.normal(0, 0.5, 100)  # Add some noise
)

# Step 2: Normalize input features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Split into training and validation
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Train neural network model
model = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=1)
model.fit(X_train, y_train)

# Step 5: Define objective function for GA
def objective_function(x):
    # x = [Temp, Feed Rate, Solids] (unnormalized)
    x_scaled = scaler.transform([x])
    predicted_moisture = model.predict(x_scaled)[0]
    return predicted_moisture  # We want to minimize this

# Step 6: Set bounds for GA parameters
varbound = np.array([
    [160, 200],  # Inlet Temp
    [5, 20],     # Feed Rate
    [10, 30]     # Solids Content
])

# Step 7: Define GA settings
algorithm_params = {
    'max_num_iteration': 50,
    'population_size': 10,
    'mutation_probability': 0.1,
    'elit_ratio': 0.02,
    'crossover_probability': 0.9,
    'parents_portion': 0.3,
    'crossover_type': 'uniform',
    'max_iteration_without_improv': None
}

# Step 8: Run the Genetic Algorithm
model_ga = ga(
    function=objective_function,
    dimension=3,
    variable_type='real',
    variable_boundaries=varbound,
    algorithm_parameters=algorithm_params
)
model_ga.run()

# Step 9: Plot fitness history (convergence)
plt.plot(model_ga.report, marker='o', linestyle='-', color='green')
plt.title("GA Optimization - Moisture Prediction")
plt.xlabel("Generation")
plt.ylabel("Predicted Moisture Content")
plt.grid(True)
plt.show()

# Step 10: Show the best results
best_input = model_ga.output_dict['variable']
best_output = model_ga.output_dict['function']
print("Best Input Parameters (Optimized):")
print(f"Inlet Temp       : {best_input[0]:.2f} °C")
print(f"Feed Rate        : {best_input[1]:.2f} L/h")
print(f"Solids Content   : {best_input[2]:.2f} %")
print(f"Predicted Moisture Content : {best_output:.4f}")