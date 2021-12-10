from tqdm import tqdm

file = open('test.txt', 'r')
input = file.read().split(',')
input = [int(x) for x in input]

print(input)

for i in tqdm(range(0, 256)):
    for idx, starfish in enumerate(input):
        starfish -= 1
        if starfish == -1:
            starfish = 6
            input.append(9)
        input[idx] = starfish

print(len(input))
