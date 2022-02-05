from collections import Counter
from tqdm import tqdm
import itertools
from functools import cache

file = open('input.txt', 'r')

input = file.read().split('\n')

template = input[0]
keys = []
values = []
tmp_dict = dict([elem.split(' -> ') for elem in input[2:]])
unique_starting_elem = ['B']
indices = [0]

for idx, key in enumerate(sorted(tmp_dict)):
    keys.append(key)
    values.append(tmp_dict[key])
    if key[0] != unique_starting_elem[-1]:
        unique_starting_elem.append(key[0])
        indices.append(idx)

insertion_rules = dict(zip(keys, values))
meta_dict = dict(zip(unique_starting_elem, indices))

@cache
def find_insertion_elem(pair, start_idx):
    for rule_pair, elem in itertools.islice(insertion_rules.items(), start_idx, start_idx + 10):
        if rule_pair == pair:
            return elem

for n in tqdm(range(10), desc='Number of steps'):
    new_template = []
    for idx in range(len(template) - 1):
        pair = template[idx] + template[idx + 1]
        new_template.append(template[idx])
        start_idx = meta_dict[template[idx]]
        elem = find_insertion_elem(pair, start_idx)
        new_template.append(elem)
    new_template.append(template[-1])
    template = new_template

values = Counter(template).values()
print(f'Solution part 1: {max(values) - min(values)}')

## Part 2
file = open('input.txt', 'r')

input = file.read().split('\n')

template = input[0]

@cache
def count(pair, step):
    if step == 40 or pair not in insertion_rules:
        return Counter()
    step += 1
    new_element = insertion_rules[pair]
    new_counter = Counter(new_element)
    new_counter.update(count(pair[0] + new_element, step))
    new_counter.update(count(new_element + pair[1], step))
    return new_counter


counter = Counter(template)
for left, right in zip(template, template[1:]):
    counter.update(count(left + right, 0))

values = counter.values()
print(f'Solution part 2: {max(values) - min(values)}')

