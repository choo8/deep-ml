import numpy as np


# Calculate Covariance Matrix

# Write a Python function to calculate the covariance matrix for a given set of vectors. The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists. Additionally, provide test cases to verify the correctness of your implementation.
    

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    try:
        matrix = np.array(vectors)
    except ValueError:
        return None
    
    n = matrix.shape[1]
    means = matrix.mean(axis=1)
    centered = matrix.T - means
    return ((1 / (n - 1)) * (centered.T @ centered)).tolist()


if __name__ == "__main__":
    vectors = [[1, 2, 3], [4, 5, 6]]
    assert calculate_covariance_matrix(vectors) == [[1.0, 1.0], [1.0, 1.0]]
