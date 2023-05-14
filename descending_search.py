import util


def descending_search(dist_matrix, iter_space, initial_solution=0):
    iter = 0
    num_cities = dist_matrix.shape[0]
    if initial_solution == 0:
        initial_solution = util.generate_initial_solution(num_cities)
    x = initial_solution
    x_distance = util.calculate_total_distance(dist_matrix, x)
    distances = []

    while iter < iter_space:
        x_prim = x.copy()
        x_prim_distance = util.calculate_total_distance(dist_matrix, x_prim)

        for i in range(num_cities):
            for j in range(num_cities):
                if i != j:
                    x_s = x.copy()
                    iter += 1
                    x_s[i], x_s[j] = x_s[j], x_s[i]
                    x_s_distance = util.calculate_total_distance(dist_matrix, x_s)
                    distances.append(x_s_distance)
                    if x_s_distance < x_prim_distance:
                        x_prim = x_s
                        x_prim_distance = util.calculate_total_distance(
                            dist_matrix, x_prim
                        )
        if x_prim_distance < x_distance:
            x = x_prim
            x_distance = util.calculate_total_distance(dist_matrix, x)

    return x, x_distance
