# Import necessary libraries
import random
import numpy as np
from deap import base, creator, tools, algorithms
from scoop import futures
import matplotlib.pyplot as plt

# -------------------------------
# Define the Objective Function
# -------------------------------
# Rastrigin function - a common benchmark optimization function
def rastrigin(individual):
    A = 10
    n = len(individual)
    return A * n + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in individual]),  # Return as tuple

# -------------------------------
# GA Setup
# -------------------------------
DIMENSIONS = 5  # Number of dimensions (can be increased for complexity)

# Define fitness and individual types for minimization
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Toolbox for GA components
toolbox = base.Toolbox()

# Attribute: Random float between -5.12 and 5.12
toolbox.register("attr_float", random.uniform, -5.12, 5.12)

# Individual: List of DIMENSIONS random floats
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=DIMENSIONS)

# Population: List of individuals
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Genetic operators
toolbox.register("evaluate", rastrigin)                      # Fitness function
toolbox.register("mate", tools.cxBlend, alpha=0.5)           # Crossover
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Mutation
toolbox.register("select", tools.selTournament, tournsize=3) # Selection

# Use SCOOP for parallel execution
toolbox.register("map", futures.map)

# -------------------------------
# Run the Genetic Algorithm
# -------------------------------
# Create initial population
population = toolbox.population(n=100)

# GA parameters
NGEN = 50          # Number of generations
CXPB = 0.7         # Crossover probability
MUTPB = 0.2        # Mutation probability
best_scores = []   # To store best fitness per generation

# Evolution process
for gen in range(NGEN):
    # Apply crossover and mutation to create offspring
    offspring = algorithms.varAnd(population, toolbox, cxpb=CXPB, mutpb=MUTPB)

    # Evaluate offspring fitness in parallel
    fits = list(toolbox.map(toolbox.evaluate, offspring))

    # Assign fitness values
    for ind, fit in zip(offspring, fits):
        ind.fitness.values = fit

    # Select the next generation
    population = toolbox.select(offspring, k=len(population))

    # Record best fitness for current generation
    top1 = tools.selBest(population, 1)[0]
    best_scores.append(top1.fitness.values[0])
    print(f"Generation {gen+1}: Best Fitness = {top1.fitness.values[0]:.4f}")

# -------------------------------
# Final Output
# -------------------------------
# Best solution after all generations
best = tools.selBest(population, 1)[0]
print("\nBest solution:", best)
print("Best fitness:", best.fitness.values[0])

# Plot convergence graph
plt.plot(best_scores)
plt.title("Convergence of Genetic Algorithm (DEAP + SCOOP)")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.grid(True)
plt.show()