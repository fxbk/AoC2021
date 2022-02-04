import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')
input = [[int(char) for char in line] for line in input]

energy_levels = np.matrix(input)

flashes = 0
for i in range(100):
    energy_levels += 1
    flash_idx = np.where(energy_levels > 9)
    prev_flashes = []
    while len(flash_idx[0]) != 0:
        for idx, idy in zip(flash_idx[0], flash_idx[1]):
            if (idx, idy) not in prev_flashes:
                flashes += 1
            energy_levels[idx, idy] = 0
            if idx > 0:
                if (idx - 1, idy) not in prev_flashes:
                    energy_levels[idx - 1, idy] += 1
                if idy > 0 and (idx - 1, idy - 1) not in prev_flashes:
                    energy_levels[idx - 1, idy - 1] += 1
                if idy < energy_levels.shape[1] - 1 and (idx - 1, idy + 1) not in prev_flashes:
                    energy_levels[idx - 1, idy + 1] += 1
            if idx < energy_levels.shape[0]-1:
                if (idx + 1, idy) not in prev_flashes:
                    energy_levels[idx + 1, idy] += 1
                if idy > 0 and (idx + 1, idy - 1) not in prev_flashes:
                    energy_levels[idx + 1, idy - 1] += 1
                if idy < energy_levels.shape[1]-1 and (idx + 1, idy + 1) not in prev_flashes:
                    energy_levels[idx + 1, idy + 1] += 1
            if idy > 0 and (idx, idy - 1) not in prev_flashes:
                energy_levels[idx, idy - 1] += 1
            if idy < energy_levels.shape[1]-1 and (idx, idy + 1) not in prev_flashes:
                energy_levels[idx, idy + 1] += 1
            prev_flashes.append((idx, idy))
        flash_idx = np.where(energy_levels > 9)

print(f'Solution part 1: {flashes}')

## Part 2
energy_levels = np.matrix(input)

first_complete_flash = False
n = 0
while not first_complete_flash:
    energy_levels += 1
    flash_idx = np.where(energy_levels > 9)
    prev_flashes = []
    while len(flash_idx[0]) != 0:
        for idx, idy in zip(flash_idx[0], flash_idx[1]):
            if (idx, idy) not in prev_flashes:
                flashes += 1
            energy_levels[idx, idy] = 0
            if idx > 0:
                if (idx - 1, idy) not in prev_flashes:
                    energy_levels[idx - 1, idy] += 1
                if idy > 0 and (idx - 1, idy - 1) not in prev_flashes:
                    energy_levels[idx - 1, idy - 1] += 1
                if idy < energy_levels.shape[1] - 1 and (idx - 1, idy + 1) not in prev_flashes:
                    energy_levels[idx - 1, idy + 1] += 1
            if idx < energy_levels.shape[0]-1:
                if (idx + 1, idy) not in prev_flashes:
                    energy_levels[idx + 1, idy] += 1
                if idy > 0 and (idx + 1, idy - 1) not in prev_flashes:
                    energy_levels[idx + 1, idy - 1] += 1
                if idy < energy_levels.shape[1]-1 and (idx + 1, idy + 1) not in prev_flashes:
                    energy_levels[idx + 1, idy + 1] += 1
            if idy > 0 and (idx, idy - 1) not in prev_flashes:
                energy_levels[idx, idy - 1] += 1
            if idy < energy_levels.shape[1]-1 and (idx, idy + 1) not in prev_flashes:
                energy_levels[idx, idy + 1] += 1
            prev_flashes.append((idx, idy))
        flash_idx = np.where(energy_levels > 9)
    if len(set(prev_flashes)) == energy_levels.shape[0] * energy_levels.shape[1]:
        first_complete_flash = True
    n += 1

print(f'Solution part 2: {n}')
