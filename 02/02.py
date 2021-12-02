import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')
print(input)

directions = [x[-3::-1][::-1] for x in input]
values = [int(x[-1]) for x in input]
print(directions)
print(values)

pos = np.array([0, 0])
for direction, value in zip(directions, values):
    if direction == 'forward':
        pos[0] += value
    if direction == 'down':
        pos[1] += value
    if direction == 'up':
        pos[1] -= value

print(np.prod(pos))

# part2
aim = 0
pos = np.array([0, 0])
for direction, value in zip(directions, values):
    if direction == 'forward':
        pos[0] += value
        pos[1] += aim * value
    if direction == 'down':
        aim += value
    if direction == 'up':
        aim -= value

print(np.prod(pos))

