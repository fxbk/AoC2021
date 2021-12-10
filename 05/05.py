import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')

lines = [[[int(x) for x in coord.split(',')] for coord in line.split(' -> ')] for line in input]

def find_vents_lines(lines, consider_diagonal):
    diagram = np.zeros((1000, 1000))  # could be problematic if dimensions too high, but should be fine here
    for line in lines:
        if line[0][1] == line[1][1]:  # horizontal line
            start = min(line[1][0], line[0][0])
            end = max(line[1][0], line[0][0])
            for elem in np.arange(start, end + 1):
                diagram[line[0][1], elem] += 1
        elif line[0][0] == line[1][0]:  # vertical line
            start = min(line[1][1], line[0][1])
            end = max(line[1][1], line[0][1])
            for elem in np.arange(start, end + 1):
                diagram[elem, line[0][0]] += 1
        elif consider_diagonal:

            xs, xe = line[0][0], line[1][0]
            ys, ye = line[0][1], line[1][1]
            xPoints = np.arange(xs, xe + 1) if line[1][0] > line[0][0] else np.arange(xs, xe - 1, -1)
            yPoints = np.arange(ys, ye + 1) if ye > ys else np.arange(ys, ye - 1, -1)

            for i in range(max(len(xPoints), len(yPoints))):
                x = xPoints[i % len(xPoints)]
                y = yPoints[i % len(yPoints)]
                diagram[x, y] += 1

    return diagram


print(sum(sum(find_vents_lines(lines, False) >= 2)))

print(sum(sum(find_vents_lines(lines, True) >= 2)))
