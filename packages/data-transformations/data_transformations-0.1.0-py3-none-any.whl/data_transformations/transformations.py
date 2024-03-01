import numpy as np

def transpose2d(input_matrix):
    return [list(row) for row in zip(*input_matrix)]


def window1d(input_array, size, shift=1, stride=1):
    windows = []
    for i in range(0, len(input_array) - size + 1, shift):
        window = input_array[i:i + size]
        windows.append(window)
    return windows

def convolution2d(input_matrix, kernel, stride=1):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    output_matrix = np.zeros((output_height, output_width))

    for i in range(0, input_height - kernel_height + 1, stride):
        for j in range(0, input_width - kernel_width + 1, stride):
            output_matrix[i // stride, j // stride] = np.sum(input_matrix[i:i + kernel_height, j:j + kernel_width] * kernel)

    return output_matrix
