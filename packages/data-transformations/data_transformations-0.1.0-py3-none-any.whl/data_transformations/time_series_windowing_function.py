import numpy as np

def window_1d(input_array, size, shift=1, stride=1):
    """
    Apply 1-dimensional windowing to a given array.

    Parameters:
    - input_array (numpy.ndarray): The input 1D array (time series).
    - size (int): The size of the window.
    - shift (int, optional): The amount to shift the window at each step. Default is 1.
    - stride (int, optional): The stride between consecutive windows. Default is 1.

    Returns:
    - list of numpy.ndarray: List of windowed arrays.
    """
    windows = []
    for i in range(0, len(input_array) - size + 1, shift):
        window = input_array[i:i + size:stride]
        windows.append(window)
    return windows

# Generate a random 1D array representing a time series
time_series = np.random.rand(10)
print("Original Time Series:")
print(time_series)

# Apply windowing with a window size of 3, shift of 2, and stride of 1
windowed_series = window_1d(time_series, size=3, shift=2, stride=1)
print("\nWindowed Time Series:")
print(windowed_series)
