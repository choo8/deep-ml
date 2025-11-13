import numpy as np


# Scalar Multiplication of a Matrix

# Write a Python function that multiplies a matrix by a scalar and returns the result.

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return (np.array(matrix) * scalar).tolist()


if __name__ == "__main__":
	matrix = [[1, 2], [3, 4]]
	scalar = 2
	assert scalar_multiply(matrix, scalar) == [[2, 4], [6, 8]]
