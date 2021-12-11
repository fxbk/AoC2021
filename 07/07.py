import numpy as np
import scipy.special

file = open('input.txt', 'r')
input = file.read().split(',')
input = [int(x) for x in input]

input = np.array(input)

print(int(sum(np.abs(input-np.median(input)))))

# part 2
min_number = 0
min_fuel = np.inf
for number in range(0, max(input)):
    fuel = sum(scipy.special.binom(np.abs(input-number)+1, 2))
    if fuel < min_fuel:
        min_muber = number
        min_fuel = fuel

print(int(min_fuel))
print(min_muber)
