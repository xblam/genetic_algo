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
POPULATION = 1000
MUTATE_RATE = 0.01
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

# get the weight to make sure that knapsack can actually hold, do this by adding weight of box if have box
def weight(individual):
    total_weight = sum(BOXES[i]["weight"] for i in range(NUM_BOXES) if individual[i] == 1)
    return total_weight

# same thing as weight but with val call this fitness, make sure if we are over weight limit we get 0
def fitness(individual):
    if weight(individual) > 250:
        return 0
    total_value = sum(BOXES[i]["value"] for i in range(NUM_BOXES) if individual[i] == 1)
    return total_value

# make the initial population
def initialize_population():
    population = []
    for _ in range(POPULATION):
        individual = [random.randint(0, 1) for _ in range(NUM_BOXES)] # randomly choose boxes
        population.append(individual) 
    for i in population:
        print(fitness(i))
    return population

# select out of a group of 10 to reproduce, standard tournament selection worsk without replacement
def tournament_selection(population):
    selected = []
    for _ in range(POPULATION // 2 ): # this will also be where we do the culling
        competitors = random.sample(population, 10)  # choose the best of random sample of 10
        best = max(competitors, key=fitness)
        selected.append(best)
    return selected

# crossover will stay simple,  it will just be a combination of the 2 parents
def crossover(parent1, parent2):
    point = random.randint(1, NUM_BOXES - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    for i in range(NUM_BOXES):
        if random.random() < MUTATE_RATE: # this one is chosen to mutate
            individual[i] = 1 - individual[i] # flip the box if mutate
    return individual



# now find the combination of boxes that leads to the max weight
def genetic_algorithm():

    # initialize the population
    population = initialize_population()

    for curr_gen in range(GENERATIONS):

        # we are going to sample select the best ones and have them reproduce
        selected = tournament_selection(population)

        #reproducing from selection
        offspring = []
        for i in range(0, len(selected), 2):
            if i + 1 < len(selected): # error from going out of bounds so put this here
                child1, child2 = crossover(selected[i], selected[i + 1])
                offspring.append(child1)
                offspring.append(child2)

        # mutate all the kids
        for i in range(len(offspring)):
            offspring[i] = mutate(offspring[i])
        # print(len(offspring))
        
        # now combine children with selected
        population = selected + offspring
        # print(len(population))

        best_solution = max(population, key=fitness)

        print(f"Generation: {curr_gen}, best solution: {best_solution}, weight: {weight(best_solution)}, score: {fitness(best_solution)}")
    return best_solution



if __name__ == "__main__":
    genetic_algorithm()