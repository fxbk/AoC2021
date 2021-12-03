import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')
values = [[[int(s) for s in x]] for x in input]
values = np.array(values)

threshold = len(input) / 2
sum_values = np.sum(values, axis=0)

gamma_bin = (sum_values >= int(threshold)).astype(int)
epsilon_bin = (sum_values < threshold).astype(int)
gamma = gamma_bin.dot(2**np.arange(gamma_bin.size)[::-1])[0]
epsilon = epsilon_bin.dot(2**np.arange(epsilon_bin.size)[::-1])[0]

print(gamma*epsilon)

# Part 2


def calculate_levels(values, larger):
    remaining_values = values
    i = 0
    while len(remaining_values) > 1:
        threshold = remaining_values.shape[0] / 2
        sum_values = np.sum(remaining_values, axis=0)

        if larger:
            binary = (sum_values >= threshold).astype(int)
        else:
            binary = (sum_values < threshold).astype(int)

        idx = remaining_values[:, :, i] == binary[0][i]
        remaining_values = remaining_values[idx]
        remaining_values = np.expand_dims(remaining_values, axis=1)
        i += 1
    return remaining_values.dot(2**np.arange(remaining_values.size)[::-1])[0, 0]


oxygen_level = calculate_levels(values, True)
scrubber = calculate_levels(values, False)
print(oxygen_level * scrubber)
