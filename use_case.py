import random
from time import perf_counter

import numpy as np
import pandas as pd
from tqdm import tqdm

import util
from descending_search import descending_search
from generator import RandomNumberGenerator
from simulated_annealing import simulated_annealing


def populate_distance_matrix(N, gen):
    D = np.full(shape=(N, N), fill_value=np.nan)
    n = D.shape[0]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            D[i, j] = gen.nextInt(1, 30)
    return D


# TODO check how initial temperature and cooling_rate bias the result
# TODO check how iter_space bias the result
# TODO visualise distances list to show how look the exploration


seed_values = [1, 42, 666, 2137, 321, 1435][:2]
matrix_sizes = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][:2]

init_temp_values = [1_000, 1_500, 2_000][:2]
cooling_rate_values = [0.9, 0.95, 0.99][:2]
iter_space_values = [1_000, 3_000, 7_000, 10_000][:2]

print(" Simulated annealing ".center(80, "="))

sa_total_iters = (
    len(seed_values)
    * len(matrix_sizes)
    * len(init_temp_values)
    * len(cooling_rate_values)
    * len(iter_space_values)
)
sa_pbar = tqdm(total=sa_total_iters)
sa_iter_results = []
for seed in seed_values:
    random.seed(seed)
    for msize in matrix_sizes:
        gen = RandomNumberGenerator(seedVaule=seed)
        dist_matrix = populate_distance_matrix(msize, gen)
        for init_temp in init_temp_values:
            for cooling_rate in cooling_rate_values:
                for iter_space in iter_space_values:
                    intitial_order = util.generate_initial_solution(msize)

                    t0 = perf_counter()

                    # distances is the list of all case that we checked
                    best_order, best_distance, distances = simulated_annealing(
                        dist_matrix,
                        init_temp,
                        cooling_rate,
                        iter_space,
                        intitial_order,
                    )

                    sa_iter_results.append(
                        {
                            "Seed": seed,
                            "MatrixSize": msize,
                            "InitTemp": init_temp,
                            "CoolingRate": cooling_rate,
                            "IterSpace": iter_space,
                            "Path": best_order,
                            "Length": best_distance,
                            "Time": perf_counter() - t0,
                        }
                    )
                    sa_pbar.update()
sa_pbar.close()

sa_results_df = pd.DataFrame.from_dict(sa_iter_results)
sa_out = "data/simulated_annealing_results.csv"
sa_results_df.to_csv(sa_out)
print(f"Results of simulated annealing saved to {sa_out}\n\n")


print(" Descending search ".center(80, "="))

ds_total_iters = len(seed_values) * len(matrix_sizes) * len(iter_space_values)
ds_pbar = tqdm(total=ds_total_iters)
ds_iter_results = []
for seed in seed_values:
    random.seed(seed)
    for msize in matrix_sizes:
        gen = RandomNumberGenerator(seedVaule=seed)
        dist_matrix = populate_distance_matrix(msize, gen)
        for init_temp in init_temp_values:
            for cooling_rate in cooling_rate_values:
                for iter_space in iter_space_values:
                    intitial_order = util.generate_initial_solution(msize)

                    t0 = perf_counter()

                    # distances is the list of all case that we checked
                    best_order, best_distance = descending_search(
                        dist_matrix, iter_space, intitial_order
                    )

                    ds_iter_results.append(
                        {
                            "Seed": seed,
                            "MatrixSize": msize,
                            "IterSpace": iter_space,
                            "Path": best_order,
                            "Length": best_distance,
                            "Time": perf_counter() - t0,
                        }
                    )
                    ds_pbar.update()
ds_pbar.close()

ds_results_df = pd.DataFrame.from_dict(ds_iter_results)
ds_out = "data/descending_search_results.csv"
ds_results_df.to_csv(ds_out)
print(f"Results of descending search saved to {ds_out}\n\n")
