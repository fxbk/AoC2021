from tqdm import tqdm
import numpy as np


file = open('test.txt', 'r')
input = file.read().split(',')
input = [int(x) for x in input]

input = np.array([3])
count = 0
for i in tqdm(range(0, 80)):
    input -= 1
    new_starfish = sum(np.where(input == -1, 1, 0))
    count += new_starfish
    input = np.where(input == -1, 6, input)
    input = np.concatenate((input, np.full(new_starfish, 8)), axis=None)

print(count)
print(len(input))
