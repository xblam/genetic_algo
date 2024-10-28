# make up an imaginary knapsack
import random



# Here's an outline for using a genetic algorithm (GA) to solve the Knapsack problem:

# 1. Define the Problem and Set Up Parameters
# Knapsack Problem: Given a set of items, each with a weight and a value, select a subset to maximize total value without exceeding a weight limit.
# Parameters:
# Population size: Number of potential solutions (individuals).
# Mutation rate: Probability of mutating an individual.
# Crossover rate: Probability of combining two individuals.
# Generations: Number of iterations.


# constants
MAX_WEIGHT = 250
GENERATIONS = 100
POPULATION = 100
BOXES = [
    {"value": 6, "weight": 20},
    {"value": 5, "weight": 30},
    {"value": 8, "weight": 60},
    {"value": 7, "weight": 90},
    {"value": 6, "weight": 50},
    {"value": 9, "weight": 70},
    {"value": 4, "weight": 30},
    {"value": 5, "weight": 30},
    {"value": 4, "weight": 70},
    {"value": 9, "weight": 20}, 
    {"value": 2, "weight": 20}, 
    {"value": 1, "weight": 60}  
]
NUM_BOXES = len(BOXES)

# get the weight to make sure that knapsack can actually hold
def weight(individual):
    total_weight = sum(BOXES[i]["weight"] for i in individual if individual[i] == 1)
    return total_weight

# if we are under the weight limit then the fitness will just be the value of boxes. If overweight we get 0 (do not like)
def fitness(individual):
    if weight(individual) > 250:
        return 0
    total_value = sum(BOXES[i]["value"] for i in individual if individual[i] == 1)
    return total_value


def initialize_population():
    population = []
    pop_count = 0

    for _ in range(POPULATION):
        individual = [random.randint(0, 1) for _ in range(NUM_BOXES)] # randomly choose boxes
        population.append(individual) 

    return population

# now find the combination of boxes that leads to the max wieght
def genetic_algorithm():

    # initialize the population
    population = initialize_population()

    # make fitness function
    
    # once we get the fitness score then we can choose the best ones to reproduce?
    
    # make a fitness functino so taht we can judge how good their performance is

    # find a way to choose the parents for the crossover

    # make new offspring with the parents

    # apply mutation to the offspring

    # cull the population by 50%

if __name__ == "__main__":
    genetic_algorithm()