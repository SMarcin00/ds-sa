import random
import math
import util

def simulated_annealing(dist_matrix, initial_temperature, cooling_rate, iter_space, initial_solution=0):
    i = 0
    num_cities = dist_matrix.shape[0]
    if initial_solution == 0:
        initial_solution = util.generate_initial_solution(num_cities)
    current_order = initial_solution
    current_distance = util.calculate_total_distance(dist_matrix, current_order)

    best_order = None
    best_distance = float('inf')

    temperature = initial_temperature
    distances = []

    while i < iter_space:
        new_order = current_order.copy()
        i += 1

        city1, city2 = random.sample(range(num_cities), 2)
        new_order[city1], new_order[city2] = new_order[city2], new_order[city1]

        new_distance = util.calculate_total_distance(dist_matrix, new_order)
        distances.append(new_distance)

        delta_distance = new_distance - current_distance
        acceptance_prob = math.exp(-delta_distance / temperature)

        if delta_distance < 0 or random.random() < acceptance_prob:
            current_order = new_order
            current_distance = new_distance

        if current_distance < best_distance:
            best_order = current_order.copy()
            best_distance = current_distance

        temperature *= cooling_rate

    return best_order, best_distance, distances


