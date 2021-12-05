import numpy as np

file = open('input.txt', 'r')
input = file.read().split('\n')

numbers = input[0].split(',')

# extract boards
boards = []
board = []
for elem in input[2::]:
    # new board
    if elem == '':
        boards.append(board)
        board = []
        continue
    line = elem.split(' ')
    line = [int(x) for x in line if x != '']
    board.append(line)

boards.append(board)

def find_bingo_board(numbers, boards):
    for number_idx, number in enumerate(numbers):
        number = int(number)
        for board_idx, board in enumerate(boards):
            for line_idx, line in enumerate(board):
                counter_bingo_row = 0
                counter_bingo_column = 0
                for grid_number_idx, grid_number in enumerate(line):
                    if grid_number == number:
                        boards[board_idx][line_idx][grid_number_idx] = 'x'
                    if grid_number == 'x':
                        counter_bingo_row += 1
                        counter_bingo_column = 0
                        for line_idx2, line2 in enumerate(board):
                            if line2[grid_number_idx] == 'x':
                                counter_bingo_column += 1
                if counter_bingo_row == len(line) or counter_bingo_column == len(line):
                    print('bingo')
                    return boards[board_idx], int(numbers[number_idx-1]), int(numbers[number_idx]),\
                           board_idx, numbers[number_idx:]


bingo_board, bingo_number, _, _, _ = find_bingo_board(numbers, boards)
bingo_board = [[0 if x == 'x' else x for x in line] for line in bingo_board]

print(bingo_number)
print(np.array(bingo_board).sum() * bingo_number)

# Part 2

while len(boards) > 1:
    _, _, _, bingo_board_idx, bingo_numbers = find_bingo_board(numbers, boards)
    boards = [board for board_idx, board in enumerate(boards) if board_idx != bingo_board_idx]

# Last board does not have to be bingo
bingo_board, _, bingo_number, _, _ = find_bingo_board(bingo_numbers, boards)
bingo_board = [[0 if x == 'x' else x for x in line] for line in bingo_board]
bingo_board = [[0 if x == bingo_number else x for x in line] for line in bingo_board]
print(bingo_number)
print(np.array(bingo_board).sum())
print(np.array(bingo_board).sum() * bingo_number)
