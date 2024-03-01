import numpy as np

def transpose_2d(input_matrix):
    """
    Transpose a 2D matrix.

    Parameters:
    - input_matrix (list of lists): The input matrix to be transposed.

    Returns:
    - list of lists: The transposed matrix.
    """
    return [list(row) for row in zip(*input_matrix)]

# Generate a random 3x3 matrix
random_matrix = np.random.rand(3, 3)
print("Original Matrix:")
print(random_matrix)

# Transpose the matrix using the transpose_2d function
transposed_matrix = transpose_2d(random_matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)
