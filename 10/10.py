from collections import Counter

file = open('input.txt', 'r')
input = file.read().split('\n')

def find_illegal_brackets(sequence):
    open_brackets = []
    for bracket in sequence:
        if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
            open_brackets.append(bracket)
        else:
            if bracket == ')':
                if open_brackets[-1] != '(':
                    return bracket
            elif bracket == ']':
                if open_brackets[-1] != '[':
                    return bracket
            elif bracket == '}':
                if open_brackets[-1] != '{':
                    return bracket
            elif bracket == '>':
                if open_brackets[-1] != '<':
                    return bracket
            open_brackets.pop()
    return None


illegal_brackets = []
for sequence in input:
    illegal_bracket = find_illegal_brackets(sequence)
    if illegal_bracket is not None:
        illegal_brackets.append(illegal_bracket)

result = 0
for bracket, value in Counter(illegal_brackets).items():
    if bracket == ')':
        result += value*3
    elif bracket == ']':
        result += value * 57
    elif bracket == '}':
        result += value * 1197
    elif bracket == '>':
        result += value * 25137

print(f'Result part 1: {result}')

## Part 2

def find_missing_brackets(sequence):
    open_brackets = []
    for bracket in sequence:
        if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
            open_brackets.append(bracket)
        else:
            open_brackets.pop()
    return open_brackets

scores = []
for sequence in input:
    if find_illegal_brackets(sequence) is not None:
        continue
    missing_brackets = find_missing_brackets(sequence)[::-1]
    score = 0
    for bracket in missing_brackets:
        score *= 5
        if bracket == '(':
            score += 1
        elif bracket == '[':
            score += 2
        elif bracket == '{':
            score += 3
        elif bracket == '<':
            score += 4
    scores.append(score)

print(f'Result part 2: {sorted(scores)[len(scores) // 2]}')
