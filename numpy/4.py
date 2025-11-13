import numpy as np


# Calculate Mean by Row or Column

# Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == "row":
		return np.array(matrix).mean(axis=1).tolist()
	elif mode == "column":
		return np.array(matrix).mean(axis=0).tolist()


if __name__ == "__main__":
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	mode = 'column'
	assert calculate_matrix_mean(matrix, mode) == [4.0, 5.0, 6.0]
