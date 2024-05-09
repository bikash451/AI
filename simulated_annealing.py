import math
import random

def objective_function(x):
    return x ** 2

def simulated_annealing(obj_func, initial_solution, temperature, cooling_rate, max_iterations):
    current_solution = initial_solution
    current_energy = obj_func(current_solution)

    best_solution = current_solution
    best_energy = current_energy

    for iteration in range(max_iterations):
        temperature *= cooling_rate
        if temperature < 1e-6:
            break

        neighbor_solution = current_solution + random.uniform(-1, 1)
        neighbor_energy = obj_func(neighbor_solution)

        energy_delta = neighbor_energy - current_energy
        if energy_delta < 0 or random.random() < math.exp(-energy_delta / temperature):
            current_solution = neighbor_solution
            current_energy = neighbor_energy

        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

    return best_solution

initial_solution = 10  
initial_temperature = 100 
cooling_rate = 0.99 
max_iterations = 1000

best_solution = simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, max_iterations)
print("Best solution:", best_solution)
print("Best energy:", objective_function(best_solution))