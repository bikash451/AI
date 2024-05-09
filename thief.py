import random

items = {
    "A": [2, 3],
    "B": [3, 5],
    "C": [4, 7],
    "D": [5, 9]
}

initial_population = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]

max_weight = 9

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

def crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_points = {"C": 0, "A": 1, "D": 2, "B": 3}
    mutated_chromosome = chromosome[:]
    bit_to_mutate = ["C", "A", "D", "B"]
    for bit in bit_to_mutate:
        if random.random() < 0.5:
            mutated_chromosome[mutation_points[bit]] = 1 - chromosome[mutation_points[bit]]
    return mutated_chromosome

def get_best(population):
    fitness_values = [calculate_fitness(chromosome) for chromosome in population]
    max_index = fitness_values.index(max(fitness_values))
    return population[max_index]


population = initial_population[:]
for _ in range(4):
    population.sort(key=calculate_fitness, reverse=True)
    parent1, parent2 = population[0], population[1]
    child1, child2 = crossover(population[2], population[3])
    child1 = mutate(child1)
    population = [parent1, parent2, child1, child2]

best_solution = get_best(population)

total_weight = sum(items[item][0] for item, bit in zip(items.keys(), best_solution) if bit == 1)
total_value = sum(items[item][1] for item, bit in zip(items.keys(), best_solution) if bit == 1)

print("The best solution after 4 iterations:")
print("Items:", [item for item, bit in zip(items.keys(), best_solution) if bit == 1])
print("Total Weight:", total_weight)
print("Total Value:", total_value)
