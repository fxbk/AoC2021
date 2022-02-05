import numpy as np

file = open('input.txt', 'r')

input = file.read().split('\n')
folds = [(char.split('=')[0][-1], int(char.split('=')[1])) for char in input if char.startswith('f')]

input = [[int(elem.split(',')[0]), int(elem.split(',')[1])] for elem in input if elem != '' and not elem.startswith('f')]
input = np.array(input)

dims = input.max(axis=0)[::-1]+1
paper = np.zeros(dims)
# dim of my input is odd
paper = np.vstack((paper, np.zeros(dims[1])))

for id in input:
    paper[id[1], id[0]] = 1

for fold in folds:
    dims = paper.shape
    if fold[0] == 'y':
        for y in range(1, fold[1]+1):
            for x in range(dims[1]):
                paper[fold[1] - y, x] += paper[fold[1] + y, x]
        paper = paper[:fold[1], :]
    if fold[0] == 'x':
        for x in range(1, fold[1]+1):
            for y in range(dims[0]):
                paper[y, fold[1] - x] += paper[y, fold[1] + x]
        paper = paper[:, :fold[1]]
    print(paper)

print(f'Solution part 1: {np.sum(paper > 0)} ')
"""
For solution of part 2 run over all folds and have a look at the resulting array, best through the SciView of your editior
"""


