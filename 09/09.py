file = open('input.txt', 'r')

input = file.read().split('\n')
input = [[int(numb) for numb in line] for line in input]

print(input)
low_points = []

for idx in range(len(input)):
    for idy in range(len(input[0])):
        counter = 4
        middle = input[idx][idy]

        if idx > 0:
            if middle < input[idx-1][idy]:
                counter -= 1
        else:
            counter -= 1
        if idy > 0:
            if middle < input[idx][idy-1]:
                counter -= 1
        else:
            counter -= 1
        if idx < len(input) - 1:
            if middle < input[idx+1][idy]:
                counter -= 1
        else:
            counter -= 1

        if idy < len(input[0]) -1:
            if middle < input[idx][idy+1]:
                counter -= 1
        else:
            counter -= 1

        if counter == 0:
            low_points.append(middle)

print(sum(low_points) + len(low_points))


