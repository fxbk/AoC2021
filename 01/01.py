import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')

input = [int(x) for x in input]
input = np.array(input)
input_shifted = input[1::]

print(sum((input_shifted - input[:-1:]) > 0))

windows = np.lib.stride_tricks.sliding_window_view(input, 3)
windows = windows.sum(axis=1)

windows_shifted = windows[1::]
print(sum((windows_shifted - windows[:-1:]) > 0))
