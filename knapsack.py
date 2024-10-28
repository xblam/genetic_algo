# make up an imaginary knapsack




# Here's an outline for using a genetic algorithm (GA) to solve the Knapsack problem:

# 1. Define the Problem and Set Up Parameters
# Knapsack Problem: Given a set of items, each with a weight and a value, select a subset to maximize total value without exceeding a weight limit.
# Parameters:
# Population size: Number of potential solutions (individuals).
# Mutation rate: Probability of mutating an individual.
# Crossover rate: Probability of combining two individuals.
# Generations: Number of iterations.

# need to make the number of potential solutions per generation

# need to make the mutation rate: probability of mutating an individual

# corssover rate: change of combining two individuals

# generations: number of iterations that we will run for


# have to make a box object to keep track fo all th eboxes - the easiest way to do this would be just to make a set

MAX_WEIGHT = 250
GENERATIONS = 100
POPULATION = 100

# the boxes will just be defined by their val and weight
boxes = [
    {"value": 20, "weight": 6},   # Box 1
    {"value": 30, "weight": 5},   # Box 2
    {"value": 60, "weight": 8},   # Box 3
    {"value": 90, "weight": 7},   # Box 4
    {"value": 50, "weight": 6},   # Box 5
    {"value": 70, "weight": 9},   # Box 6
    {"value": 30, "weight": 4},   # Box 7
    {"value": 30, "weight": 5},   # Box 8
    {"value": 70, "weight": 4},   # Box 9
    {"value": 20, "weight": 9},   # Box 10
    {"value": 20, "weight": 2},   # Box 11
    {"value": 60, "weight": 1}    # Box 12
]

# now find the combination of boxes that leads to the max wieght