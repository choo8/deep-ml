import math

import numpy as np


# Solve Linear Equations using Jacobi Method

# Write a Python function that uses the Jacobi method to solve a system of linear equations given by Ax = b. The function should iterate n times, rounding each intermediate solution to four decimal places, and return the approximate solution x.

def solve_jacobi(A: list[list[int]], b: list[list[int]], n: int) -> list:
    A = np.array(A)
    b = np.array(b)

    D = np.diag(np.diag(A))
    R = A - D

    x = np.zeros(A.shape[-1])
    for _ in range(n):
        x = np.linalg.inv(D) @ (b - (R @ x))

    return x


def assert_lists_are_close(list1: list[int], list2: list[int], rel_tol=1e-3, abs_tol=0.0):
    """
    Asserts that all corresponding elements in two lists are close.
    """
    # Check that lists have the same length
    assert len(list1) == len(list2)
    
    # Use all() with nested generator expressions for the closeness check
    all_close = all(
        math.isclose(elem1, elem2, rel_tol=rel_tol, abs_tol=abs_tol)
        for elem1, elem2 in zip(list1, list2)
    )
    
    assert all_close, "Not all elements in the lists are close within the specified tolerance."


if __name__ == "__main__":
    A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
    b = [-1, 2, 3]
    n = 2
    assert_lists_are_close(solve_jacobi(A, b, n), [0.146, 0.2032, -0.5175])
