import numpy as np


# Transpose of a Matrix

# Write a Python function that computes the transpose of a given matrix.

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return np.array(a).T.tolist()


if __name__ == "__main__":
    a = [[1,2,3],[4,5,6]]
    assert transpose_matrix(a) == [[1,4],[2,5],[3,6]]
