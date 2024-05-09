import random

# Items that can be put in the knapsack [weight, value]
items = {
    "A": [45, 3],
    "B": [40, 5],
    "C": [50, 8],
    "D": [90, 10]
}

# Chromosome is a 4-bit string [xA, xB, xC, xD]
# Initial population: {1 1 1 1, 1 0 0 0, 1 0 1 0, 1 0 0 1}
initial_population = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

# Maximum Capacity of the bag (W) = 100
max_weight = 100

# Function to calculate the fitness of a chromosome
def calculate_fitness(chromosome):
    total_weight = 0
    total_value = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            item = list(items.values())[i]
            total_weight += item[0]
            total_value += item[1]
    if total_weight > max_weight:
        return 0
    else:
        return total_value

# Function to perform one-point crossover
def crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation
def mutate(chromosome):
    mutation_points = {"D": 0, "C": 1, "B": 2, "A": 3}
    mutated_chromosome = chromosome[:]
    bit_to_mutate = ["D", "C", "B", "A"]
    for bit in bit_to_mutate:
        if random.random() < 0.5:
            mutated_chromosome[mutation_points[bit]] = 1 - chromosome[mutation_points[bit]]
    return mutated_chromosome

# Function to get the best chromosome from the population
def get_best(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    max_index = fitness_values.index(max(fitness_values))
    return population[max_index]

# Perform genetic evolution
population = initial_population[:]
for _ in range(10):
    parent1, parent2 = random.sample(population, 2)
    child1, child2 = crossover(parent1, parent2)
    child1 = mutate(child1)
    child2 = mutate(child2)
    population.extend([child1, child2])

best_solution = get_best(population)

# Calculate weight and value of the best solution
total_weight = sum(items[item][0] for item, bit in zip(items.keys(), best_solution) if bit == 1)
total_value = sum(items[item][1] for item, bit in zip(items.keys(), best_solution) if bit == 1)

# Output the result
print("The best solution:")
print("Items:", [item for item, bit in zip(items.keys(), best_solution) if bit == 1])
print("Total Weight:", total_weight)
print("Total Value:", total_value)
