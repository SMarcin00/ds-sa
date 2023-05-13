import random

random.seed(1)

def calculate_total_distance(dist_matrix, order):
    total_distance = 0.0
    for i in range(len(order) - 1):
        total_distance += dist_matrix[order[i]][order[i + 1]]
    return total_distance

def generate_initial_solution(num_cities):
    order = list(range(num_cities))
    random.shuffle(order)
    return order

