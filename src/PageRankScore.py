import ProbabilityMatrix as PM
import numpy as np


def page_rank_score(adj_mat, epsilon=1e-6, max_iteration=100):
    mat_tra = PM.matrice_probability(adj_mat)
    N = len(adj_mat)
    rank_score = np.ones(N) / N

    for iteration in range(max_iteration):
        new_rank_score = np.dot(rank_score, mat_tra)

        print(f"Iteration {iteration + 1}: {new_rank_score}")

        if np.linalg.norm(new_rank_score - rank_score, ord=1) <= epsilon:
            break
        rank_score = new_rank_score

    return rank_score
