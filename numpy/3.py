import numpy as np


# Reshape Matrix

# Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ]

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    try:
        return np.array(a).reshape(new_shape).tolist()
    except ValueError:
        return []


if __name__ == "__main__":
    a = [[1,2,3,4],[5,6,7,8]]
    new_shape = (4, 2)
    assert reshape_matrix(a, new_shape) == [[1, 2], [3, 4], [5, 6], [7, 8]]
