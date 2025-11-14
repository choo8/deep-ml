import math

import numpy as np


# Calculate 2x2 Matrix Inverse

# Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    matrix = np.array(matrix)
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	
    if det == 0:
        return None
    
    return ((1 / det) * np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])).tolist()


def assert_nested_lists_are_close(list1, list2, rel_tol=1e-9, abs_tol=0.0):
    """
    Asserts that all corresponding elements in two equally structured nested lists are close.
    """
    # Check that lists have the same structure (simple check for same length of sublists)
    assert len(list1) == len(list2)
    for sublist1, sublist2 in zip(list1, list2):
        assert len(sublist1) == len(sublist2)
    
    # Use all() with nested generator expressions for the closeness check
    all_close = all(
        math.isclose(elem1, elem2, rel_tol=rel_tol, abs_tol=abs_tol)
        for sublist1, sublist2 in zip(list1, list2)
        for elem1, elem2 in zip(sublist1, sublist2)
    )
    
    assert all_close, "Not all elements in the nested lists are close within the specified tolerance."


if __name__ == "__main__":
	matrix = [[4, 7], [2, 6]]
	assert_nested_lists_are_close(inverse_2x2(matrix), [[0.6, -0.7], [-0.2, 0.4]])
