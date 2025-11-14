import numpy as np


# Matrix times Matrix

# multiply two matrices together (return -1 if shapes of matrix don't align), i.e. C=A⋅B

def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    a = np.array(a)
    b = np.array(b)
	
    if a.shape[-1] != b.shape[0]:
        return -1
    
    return (a @ b).tolist()


if __name__ == "__main__":
    A = [[1,2],[2,4]]
    B = [[2,1],[3,4]]
    assert matrixmul(A, B) == [[ 8,  9],[16, 18]]
