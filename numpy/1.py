import numpy as np


# Matrix-Vector Dot Product

# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    try:
        mat = np.array(a)
        v = np.array(b)

        return (mat @ v).tolist()
    except ValueError:
        return -1


if __name__ == "__main__":
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    assert matrix_dot_vector(a, b) == [5, 10]
