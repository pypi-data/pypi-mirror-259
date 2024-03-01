import numpy as np

def convolution_2d(input_matrix, kernel, stride=1):
    """
    Perform 2-dimensional convolution on the given input matrix with the specified kernel.

    Parameters:
    - input_matrix (numpy.ndarray): The input 2D matrix.
    - kernel (numpy.ndarray): The convolution kernel.
    - stride (int, optional): The stride for the convolution operation. Default is 1.

    Returns:
    - numpy.ndarray: The resulting convolution output matrix.
    """
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    output_matrix = np.zeros((output_height, output_width))

    for i in range(0, input_height - kernel_height + 1, stride):
        for j in range(0, input_width - kernel_width + 1, stride):
            output_matrix[i // stride, j // stride] = np.sum(
                input_matrix[i:i + kernel_height, j:j + kernel_width] * kernel)

    return output_matrix


# Generate a random 4x4 input matrix
input_matrix = np.random.rand(4, 4)
print("Input Matrix:")
print(input_matrix)

# Generate a random 2x2 kernel
kernel = np.random.rand(2, 2)
print("\nKernel:")
print(kernel)

# Apply convolution with a stride of 1
output_matrix = convolution_2d(input_matrix, kernel, stride=1)
print("\nOutput Matrix:")
print(output_matrix)
