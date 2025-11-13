import numpy as np


# Calculate Eigenvalues of a Matrix

# Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	tr = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	eigenvalues = [(tr + ((tr * tr) - (4 * det)) ** 0.5) / 2, (tr - ((tr * tr) - (4 * det)) ** 0.5) / 2]

	return sorted(eigenvalues, reverse=True)


if __name__ == "__main__":
	matrix = [[2, 1], [1, 2]]
	assert calculate_eigenvalues(matrix) == [3.0, 1.0]
