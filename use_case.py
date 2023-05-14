import simulated_annealing
import descending_search
import numpy as np
from generator import RandomNumberGenerator
import util
import random

SEED = 76532
SIZE = 10

random.seed(SEED)


def populate_distance_matrix(N, gen):
    D = np.full(shape=(N, N), fill_value=np.nan)
    n = D.shape[0]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            D[i, j] = gen.nextInt(1, 30)
    return D

# Example usage

gen = RandomNumberGenerator(seedVaule=SEED)
dist_matrix = populate_distance_matrix(SIZE, gen)
initial_temperature = 1000.0 
cooling_rate = 0.999
iter_space = 10000 #it is not the number of iteration, it is the number of cases that will be checked, better halt condition that will make comparision more reliable

intitial_order = util.generate_initial_solution(SIZE)

# distances is the list of all case that we checked
best_order, best_distance, distances = simulated_annealing.simulated_annealing(dist_matrix, initial_temperature, cooling_rate, iter_space, intitial_order)
print("Best order sa:", best_order)
print("Best distance:", best_distance)

best_order, best_distance = descending_search.descending_search(dist_matrix, iter_space, intitial_order) # x at the end is initial order just to make sure we can compare two methods

print("Best order ds:", best_order)
print("Best distance:", best_distance)


#TODO check how initial temperature and cooling_rate bias the result
#TODO check how iter_space bias the result
#TODO visualise distances list to show how look the exploration

