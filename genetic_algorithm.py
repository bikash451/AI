import random

def create_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

def population(size, length):
    return [create_individual(length) for _ in range(size)]

def fitness(individual, target):
    return sum(gene == target_gene for gene, target_gene in zip(individual, target))

def selection(population, target):
    fitness_scores = [fitness(individual, target) for individual in population]
    return population[fitness_scores.index(max(fitness_scores))]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(target, population_size, mutation_rate, generations):
    pop = population(population_size, len(target))
    for _ in range(generations):
        pop = [mutation(crossover(selection(pop, target), selection(pop, target))[0], mutation_rate) for _ in range(population_size)]
        best_individual = selection(pop, target)
        if fitness(best_individual, target) == len(target):
            return best_individual

# Example usage:
target = [1, 0, 1, 0, 0, 0, 0, 0]  # Target individual
population_size = 100  # Size of the population
mutation_rate = 0.01  # Mutation rate
generations = 1000  # Number of generations

solution = genetic_algorithm(target, population_size, mutation_rate, generations)
print("Solution:", solution)