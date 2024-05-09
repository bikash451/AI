import heapq
import itertools

#calculate distance using formula of distance bw 2 points
def distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def generate_permutations(cities):
    return list(itertools.permutations(cities))

def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    total += distance(route[-1], route[0])
    return total

def a_star_tsp(cities):
    heap = []
    start_state = cities[0], (cities[0],) 
    heapq.heappush(heap, (total_distance(start_state[1]), start_state))
    while heap:
        _, (current_city, visited_cities) = heapq.heappop(heap)
        if len(visited_cities) == len(cities):
            return visited_cities
        for city in cities:
            if city not in visited_cities:
                new_route = visited_cities + (city,)
                priority = total_distance(new_route)
                heapq.heappush(heap, (priority, (city, new_route)))
    return None

cities = [(0, 0), (1, 2), (3, 1), (5, 3), (2, 4)]
solution = a_star_tsp(cities)
if solution:
    print("Optimal route found:")
    for city in solution:
        print(city)
else:
    print("No solution found.")