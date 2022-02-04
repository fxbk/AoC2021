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

print(result)